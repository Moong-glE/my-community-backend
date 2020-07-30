from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from mycomm.serializers.department import DepartmentSerializer


class DepartmentViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    serializer_class = DepartmentSerializer
