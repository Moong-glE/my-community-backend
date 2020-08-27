from django.contrib.auth import authenticate
from rest_framework import serializers

from mycomm.models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password1', 'password2',
                  'student_id', 'profile_image', 'department']

    def validate(self, attrs):
        email = attrs.get('email')
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')

        if email is None or password1 is None or password2 is None:
            raise serializers.ValidationError("Please provide both email and password")
        if password1 != password2:
            raise serializers.ValidationError("The two password fields didn't match")

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password1'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password1']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email is None or password is None:
            raise serializers.ValidationError("Please provide both email and password")

        user = authenticate(email=email, password=password)

        if user and user.is_active:
            return user
        raise serializers.ValidationError("The user could not be found")
