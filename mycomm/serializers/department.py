from rest_framework import serializers

from mycomm.models.department import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'university']
