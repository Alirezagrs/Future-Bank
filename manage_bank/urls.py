from django.urls import path

from .views import TransactionView
app_name = "manage_bank"

urlpatterns = [
    path("transaction/<uuid:pk>/<uuid:account_number>/<int:amount>/<int:from_card>/<int:to_card>/",
         TransactionView.as_view(), name="transaction"),
]
