from rest_framework import serializers

from clinic.models import HealthProblem
from clinic.models import Client


class HealthProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProblem
        fields = ['id', 'name', 'degree']


class ClientSerializer(serializers.ModelSerializer):
    health_problems = HealthProblemSerializer(many=True)

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

    def create(self, validated_data):
        health_problems = validated_data.pop('health_problems')
        client = Client.objects.create(**validated_data)

        for health_problem in health_problems:
            health_problem_instance, _ = HealthProblem.objects.get_or_create(**health_problem)
            client.health_problems.add(health_problem_instance)
        
        return client