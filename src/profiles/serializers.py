from rest_framework import serializers
from .models import UserFC


class GetUserFCSerializer(serializers.ModelSerializer):
    #����� ���������� � User
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
    #����� ��������� ���������� � User
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

