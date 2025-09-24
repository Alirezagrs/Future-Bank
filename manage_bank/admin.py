from django.contrib import admin

from .models import Employees, Accounts, CurrentAcount, \
    LoanAcoount, Transactions


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "designation",
                    "hire_date", "salary_mount")
    search_fields = ("employee_code",)
    list_filter = ("hire_date",)


class AccountsAdmin(admin.ModelAdmin):
    list_display = ("count", "total_amount")


class CurrentAcountAdmin(admin.ModelAdmin):
    list_display = ("acount_number", "status", "created_at", "balance",)
    search_fields = ("acount_number",)
    list_filter = ("status", "created_at",)


class LoanAcoountAdmin(admin.ModelAdmin):
    list_display = ("acount_number", "status", "created_at", "balance",)
    search_fields = ("acount_number",)
    list_filter = ("status", "created_at",)


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ("transaction_amount", "left_amount",
                    "transactions_date", "transaction_number",)
    list_filter = ("transaction_number",)


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Accounts, AccountsAdmin)
admin.site.register(CurrentAcount, CurrentAcountAdmin)
admin.site.register(LoanAcoount, LoanAcoountAdmin)
admin.site.register(Transactions, TransactionsAdmin)
