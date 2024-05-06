from rest_framework import serializers

from .models import UserAccount


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "email")
