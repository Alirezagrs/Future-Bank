from django.urls import path

from .views import UserRegisterView, UserGetAllInformationView, \
    UserGetInformationView, UserHardDeleteInformationView, \
    UserSoftDeleteInformationView, UserUpdateInformationView

app_name = "manage_user"

urlpatterns = [
    path("registration/",
         UserRegisterView.as_view(), name="register"),

    path("getall/",
         UserGetAllInformationView.as_view(), name="getall"),

    path("get/<uuid:pk>/",
         UserGetInformationView.as_view(), name="get"),

    path("hard-delete/<uuid:pk>/",
         UserHardDeleteInformationView.as_view(), name="hard-delete"),

    path("soft-delete/<uuid:pk>/",
         UserSoftDeleteInformationView.as_view(), name="soft-delete"),

    path("update/<uuid:pk>/",
         UserUpdateInformationView.as_view(), name="update"),
]
