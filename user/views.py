from rest_framework.views import APIView, Response
from rest_framework import status

from user.models import Users

from .serializers import UserRegistrationSerializer, UserGetAllDataSerializer


class UserRegisterView(APIView):
    def post(self, request):
        user = UserRegistrationSerializer(data=request.data)  # or request.POST
        if user.is_valid():
            print(user.validated_data)
            user.create(user.validated_data)
            return Response("user has been registered", status.HTTP_200_OK)

        return Response(user.errors, status.HTTP_400_BAD_REQUEST)


class UserGetAllInformationView(APIView):
    def get(self, request):
        users = Users.objects.select_related(
            "employee").prefetch_related('accounts').all()
        user_serializer = UserGetAllDataSerializer(instance=users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
