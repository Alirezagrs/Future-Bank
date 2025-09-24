from django.db import transaction
from rest_framework.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Transactions
from user.models import Users


class TransactionView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk, account_number, amount, from_card, to_card):
        # user_with_l_account = Users.objects.prefetch_related('account').select_related("loan").prefetch_related("l_transaction").get(pk=pk)
        # user_with_c_account = Users.objects.prefetch_related('account').select_related("current").prefetch_related("c_transaction").get(pk=pk)
        user = Users.objects.prefetch_related(
            'account__loan__l_transaction',
            'account__current__c_transaction'
        ).get(pk=pk)
        with transaction.atomic():
            for acc in user.account.all():
                # loan
                if hasattr(acc, 'loan'):
                    if account_number == acc.loan.acount_number and acc.loan.balance >= amount:
                        acc.loan.balance -= amount
                        acc.total_amount -= amount
                        acc.loan.save()
                        acc.save()

                        transaction = Transactions(
                            transaction_amount=amount,
                            left_amount=acc.loan.balance,
                            from_card=from_card,
                            to_card=to_card,
                            l_account_id=acc.loan
                        )
                        transaction.save()

                # current
                if hasattr(acc, 'current'):
                    if account_number == acc.current.acount_number and acc.current.balance >= amount:
                        acc.current.balance -= amount
                        acc.total_amount -= amount

                        transaction = Transactions(
                            transaction_amount=amount,
                            left_amount=acc.current.balance,
                            from_card=from_card,
                            to_card=to_card,
                            c_account_id=acc.current
                        )
                        transaction.save()
