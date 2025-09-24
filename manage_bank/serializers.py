from rest_framework import serializers

from .models import Transactions

class TransactionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"
        extra_kwargs={
            "left_amount": {"read_only": True},
            "transaction_amount": {"write_only": True},
        }