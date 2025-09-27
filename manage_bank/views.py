from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Transactions
from user.models import Users


class TransactionView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        pk = request.get("pk")
        account_number = request.get("account_number")
        amount = request.get("amount")
        from_card = request.get("from_card")
        to_card = request.get("to_card")

        user = get_object_or_404(Users, pk=pk)
        
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
