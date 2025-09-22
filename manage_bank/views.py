from rest_framework.views import APIView, Response
from rest_framework import status

from .serializers import UserSerializer

class UserRegisterView(APIView):
    def post(self, request):
        user = UserSerializer(data=request.data) # or request.POST
        if user.is_valid():
            print(user.validated_data)
            user.create(user.validated_data)
            return Response("user has been registered", status.HTTP_200_OK)
        
        return Response(user.errors, status.HTTP_400_BAD_REQUEST)
