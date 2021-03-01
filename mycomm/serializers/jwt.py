from rest_framework import serializers

from mycomm.serializers.user import UserSerializer


class CustomJWTSerializer:
    token = serializers.CharField()
    user = serializers.SerializerMethodField

    @staticmethod
    def get_user(obj):
        user_serializer = UserSerializer(obj['user'])
        return user_serializer.data
