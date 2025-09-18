from uuid import uuid4

from django.db import models

from user.models import Users


class Employees(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    employee_code = models.PositiveIntegerField()
    salary_mount = models.DecimalField(max_digits=8, decimal_places=0) # toman
    hire_date = models.DateTimeField()
    designation = models.CharField(max_length=20)
    user_id = models.OneToOneField(
        to=Users, on_delete=models.CASCADE, related_name="employee"
    )
