from django.contrib.auth import authenticate
from rest_framework import serializers

from mycomm.models.department import Department
from mycomm.models.user import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'student_id', 'profile_image', 'department']

    @staticmethod
    def get_cleaned_data(validated_data):
        return {
            'username': validated_data.get('username', ''),
            'password': validated_data.get('password', ''),
            'email': validated_data.get('email', ''),
            'student_id': validated_data.get('student_id', ''),
            'profiled_image': validated_data.get('profile_image', ''),
            'department': validated_data.get('department', 0),
        }

    def create(self, validated_data):
        clean_data = self.get_cleaned_data(validated_data)
        user = User()
        user.username = clean_data.get('username')
        user.set_password(clean_data.get('password'))
        user.email = clean_data.get('email')
        user.student_id = clean_data.get('student_id')
        user.profile_image = clean_data.get('profiled_image')
        try:
            user.department = Department.objects.get(id=clean_data.get('department'))
        except Department.DoesNotExist:
            user.department = None
        user.save()
        return user


class UserSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        attrs['user'] = authenticate(username=username, password=password)
        return attrs


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',
                  'student_id', 'profile_image', 'department']
