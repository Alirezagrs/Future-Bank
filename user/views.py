from uuid import UUID

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from user.models import Users
from .serializers import UserRegistrationSerializer, UserGetAllDataSerializer


# create user
class UserRegisterView(APIView):
    def post(self, request):
        user = UserRegistrationSerializer(data=request.data)  # or request.POST
        if user.is_valid():
            # used self.user for ref count, not refcount=0 after running.
            self.user=user.create(user.validated_data)
            token, created = Token.objects.get_or_create(user=self.user)
            return Response("user has been registered", status.HTTP_201_CREATED)

        return Response(user.errors, status.HTTP_400_BAD_REQUEST)


# get all users
class UserGetAllInformationView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self, request):
        users = Users.objects.select_related(
            "employee").prefetch_related('account').filter(is_active=True).all()
        user_serializer = UserGetAllDataSerializer(instance=users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


# get specific user
class UserGetInformationView(APIView):
    def get(self, request, pk: UUID):
        user = Users.objects.select_related(
            'employee').prefetch_related('account').get(pk=pk, is_active=True)
        user_serializer = UserGetAllDataSerializer(user)
        return Response(user_serializer.data, status.HTTP_200_OK)


# patch-update specific user
class UserUpdateInformationView(APIView):
    def patch(self, request, pk: UUID):
        user = get_object_or_404(Users, pk=pk)
        user_serializer = UserGetAllDataSerializer(
            user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# hard-delete specific user
class UserHardDeleteInformationView(APIView):
    def delete(self, request, pk: UUID):
        user = get_object_or_404(Users, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# soft-delete specific user
class UserSoftDeleteInformationView(APIView):
    def delete(self, request, pk: UUID):
        user = get_object_or_404(Users, pk=pk)
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
