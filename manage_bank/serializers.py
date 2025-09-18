from rest_framework import serializers

from user.models import Users

class UserSerializer(serializers.ModelSerializer):
    # must not use password1 because we have password  in user model
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = "__all__"
    
    def validate(self, data):
        if data["password"] == data["password2"]:
            return data
        return serializers.ValidationError("passwords not match!")
    
    def create(self, validated_data):
        # no need to save field password2 in db
        validated_data.pop("password2")
        user = Users.objects.create_user(**validated_data)
        return user


        