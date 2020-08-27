from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

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
        self.serializer.validate(request)

        self.login()
        return self.get_response()


class MycommRegisterView(RegisterView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validate(serializer.validated_data)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user),
                        status=HTTP_201_CREATED,
                        headers=headers)
