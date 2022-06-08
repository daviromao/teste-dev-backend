from rest_framework import serializers

from clinic.models import HealthProblem
from clinic.models import Client

from clinic.utils import associate_client_with_health_problems_list, calculate_score_from_health_problems


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
            'updated_at',
            'score',
        ]

        read_only_fields = ['score']

    def create(self, validated_data):
        health_problems = validated_data.pop('health_problems')
        client = Client.objects.create(**validated_data)

        associate_client_with_health_problems_list(client, health_problems)
        client.score = calculate_score_from_health_problems(health_problems)

        client.save()
        
        return client

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.gender = validated_data.get('birthdate', instance.gender)

        if 'health_problems' in validated_data:
            instance.health_problems.clear()

            health_problems = validated_data.pop('health_problems')
            
            associate_client_with_health_problems_list(client=instance, health_problems=health_problems)
            instance.score = calculate_score_from_health_problems(health_problems)

        instance.save()

        return instance