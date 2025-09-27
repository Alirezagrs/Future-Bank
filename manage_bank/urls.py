from django.urls import path

from .views import TransactionView

app_name = "manage_bank"

urlpatterns = [
    path("transaction/", TransactionView.as_view(), name="transaction"),
]
