from uuid import uuid4

from django.db import models

from user.models import Users


class Employees(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee_code = models.PositiveIntegerField(unique=True, db_index=True)
    salary_mount = models.DecimalField(max_digits=8, decimal_places=0)  # toman
    hire_date = models.DateTimeField()
    designation = models.CharField(max_length=20)
    user = models.OneToOneField(
        to=Users, on_delete=models.CASCADE, related_name="employee"
    )


class Accounts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    count = models.PositiveSmallIntegerField(null=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0)
    user = models.ForeignKey(
        to=Users, on_delete=models.CASCADE, related_name="account"
        )


# حساب پس انداز
class LoanAcoount(models.Model):
    id = models.OneToOneField(
        primary_key=True, to=Accounts, on_delete=models.CASCADE
        )
    acount_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=10, decimal_places=0)


# حساب جاری
class CurrentAcount(models.Model):
    id = models.OneToOneField(
        primary_key=True, to=Accounts, on_delete=models.CASCADE
        )
    acount_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.DecimalField(max_digits=8, decimal_places=0)


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    transaction_amount = models.PositiveIntegerField()
    left_amount = models.PositiveIntegerField()
    transactions_date = models.DateTimeField()
    transaction_number = models.CharField(
        default=uuid4, unique=True, db_index=True)
    l_account_id = models.ForeignKey(to=LoanAcoount, on_delete=models.CASCADE)
    c_account_id = models.ForeignKey(
        to=CurrentAcount, on_delete=models.CASCADE
    )
