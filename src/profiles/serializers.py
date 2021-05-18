from rest_framework import serializers
from .models import UserFC


class GetUserFCSerializer(serializers.ModelSerializer):
    #Вывод информации о User
    class Meta:
        model = UserFC
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )


class GetUserFCPublicSerializer(serializers.ModelSerializer):
    #Вывод публичной информации о User
    class Meta:
        model = UserFC
        exclude = (
            "password",
            "phone",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )

