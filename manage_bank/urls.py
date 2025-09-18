from django.urls import path

from .views import UserRegisterView

app_name = "manage_bank"

urlpatterns = [
    path("registration/", UserRegisterView.as_view(), name="register")
]