from django.urls import path
from rest_framework import routers

from mycomm.views.department import DepartmentViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('departments', DepartmentViewSet, basename='departments')

urlpatterns = [] + router.urls
