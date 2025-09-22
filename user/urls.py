from django.urls import path

from .views import UserRegisterView, UserGetAllInformationView

app_name = "manage_user"

urlpatterns = [
    path("registration/", UserRegisterView.as_view(), name="register"),
    path("getall/", UserGetAllInformationView.as_view(), name="getall"),
]