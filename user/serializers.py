# 데이터를 펼쳐준다 (직렬화)

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    mail = serializers.CharField(required=True)
    is_active = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    update_at = serializers.DateTimeField(required=True)

    class Meta:
        model = User
        fields = (
            'user_name',
            'password',
            'mail',
            'is_active',
            'created_at',
            'update_at',
        )
