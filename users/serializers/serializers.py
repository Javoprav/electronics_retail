from rest_framework import serializers
from users.models import User


class ForAuthUserSerializers(serializers.ModelSerializer):
    """Сериализатор для Пользователя"""
    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'city')


class ForCreateUserSerializers(serializers.ModelSerializer):
    """Сериализатор для создания Пользователя"""
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }
