from django.contrib import admin

from .models import Employees, Accounts
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "designation", "hire_date", "salary_mount")
    search_fields = ("employee_code",)
    list_filter = ("hire_date",)

class AccountsAdmin(admin.ModelAdmin):
    list_display = ("count", "total_amount")
    
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Accounts, AccountsAdmin)