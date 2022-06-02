from rest_framework import serializers

from clinic.models import HealthProblem
from clinic.models import Client


class HealthProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProblem
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    health_problems = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'birthdate',
            'gender',
            'health_problems',
            'created_at',
            'updated_at'
        ]
