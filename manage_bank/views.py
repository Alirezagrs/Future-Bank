from django.db import transaction
from rest_framework.views import APIView, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Accounts, Transactions
from user.models import Users


class TransactionView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        amount = int(request.data[0].get("amount"))
        from_account_number  = request.data[0].get("from_account")
        to_account_number  = request.data[0].get("to_account")

        with transaction.atomic():
            transaction_done = False
            from_account = Accounts.objects.select_for_update().select_related(
                "loan", "current"
            ).get(
                loan__account_number=from_account_number
            ) if Accounts.objects.filter(loan__account_number=from_account_number).exists() else Accounts.objects.select_for_update().select_related("loan", "current").get(current__account_number=from_account_number)

            to_account = Accounts.objects.select_for_update().select_related(
                "loan", "current"
            ).get(
                loan__account_number=to_account_number
            ) if Accounts.objects.filter(loan__account_number=to_account_number).exists() else Accounts.objects.select_for_update().select_related("loan", "current").get(current__account_number=to_account_number)

            if hasattr(from_account, "loan"):
                if from_account.loan.balance < amount:
                    return Response({"error": "insufficient amount"}, status=status.HTTP_400_BAD_REQUEST)
                from_account.loan.balance -= amount
                from_account.total_amount -= amount
                from_account.loan.save()
                from_account.save()
                transaction_done = True

            elif hasattr(from_account, "current"):
                if from_account.current.balance < amount:
                    return Response({"error": "insufficient amount"}, status=status.HTTP_400_BAD_REQUEST)
                from_account.current.balance -= amount
                from_account.total_amount -= amount
                from_account.current.save()
                from_account.save()
                transaction_done = True

                # current
            if hasattr(to_account, "loan"):
                to_account.loan.balance += amount
                to_account.total_amount += amount
                to_account.loan.save()
                to_account.save()
                transaction_done = True

            elif hasattr(to_account, "current"):
                to_account.current.balance += amount
                to_account.total_amount += amount
                to_account.current.save()
                to_account.save()
                transaction_done = True
                
            Transactions.objects.create(
                transaction_amount=amount,
                left_amount=(from_account.loan.balance if hasattr(from_account, "loan") else from_account.current.balance),
                from_card=from_account_number,
                to_card=to_account_number,
                l_account_id=from_account.loan if hasattr(from_account, "loan") else None,
                c_account_id=from_account.current if hasattr(from_account, "current") else None,
            )
                
            
        if transaction_done:
            return Response("transaction done successfuly", status.HTTP_200_OK)
        
        return Response("transaction failed!!!", status.HTTP_400_BAD_REQUEST)
