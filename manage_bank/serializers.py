from rest_framework import serializers

from user.models import Users

class UserRegisterSerializer(serializers.ModelSerializer):
    # must not use password1 because we have password  in user model
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = "__all__"
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords not match!")
        return data
        

    def create(self, validated_data):
        
        # no need to save field password2 in db
        # if fields which filled by user coming here and are validated
        # so i must create a user
        del validated_data["password2"]
        user = Users.objects.create_user(**validated_data)
        return user



class UserGetInformationSerializer(serializers.Serializer):
    pass