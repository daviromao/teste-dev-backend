from rest_framework import serializers

from clinic.models import HealthProblem
from clinic.models import Client
from math import e

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

        for health_problem in health_problems:
            health_problem_instance, _ = HealthProblem.objects.get_or_create(**health_problem)
            client.health_problems.add(health_problem_instance)
        

        """
            sd = soma do grau dos problemas
            score = (1 / (1 + e^-(-2.8 + sd ))) * 100
        """
        lambda_degree = lambda health_problem: health_problem.degree
        sum_degree = sum(map(lambda_degree, client.health_problems.all()))
        score = (1/ (1+e**(-(-2.8 + sum_degree)))) * 100

        client.score = score

        client.save()
        
        return client

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.gender = validated_data.get('birthdate', instance.gender)

        if 'health_problems' in validated_data:
            instance.health_problems.clear()

            health_problems = validated_data.pop('health_problems')
            for health_problem in health_problems:
                health_problem_instance, _ = HealthProblem.objects.get_or_create(**health_problem)
                instance.health_problems.add(health_problem_instance)

        """
            sd = soma do grau dos problemas
            score = (1 / (1 + e^-(-2.8 + sd ))) * 100
        """

        lambda_degree = lambda health_problem: health_problem.degree
        sum_degree = sum(map(lambda_degree, instance.health_problems.all()))
        score = (1/ (1+e**(-(-2.8 + sum_degree)))) * 100

        instance.score = score

        instance.save()

        return instance