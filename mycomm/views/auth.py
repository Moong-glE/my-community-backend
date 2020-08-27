from rest_auth.utils import jwt_encode
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

from mycomm.serializers.user import UserSerializer, UserCreateSerializer


class MycommLoginView(LoginView):
    serializer_class = UserSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.request = None
        self.serializer = None

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data,
                                              context={'request': request})
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class MycommRegisterView(RegisterView):
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.create(self.request.data)
        self.token = jwt_encode(user)
        return user
