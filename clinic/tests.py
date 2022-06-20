from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from django.test import SimpleTestCase

from datetime import date

from clinic.models import Client
from clinic.utils import calculate_score_from_health_problems


class ClientTests(APITestCase):

    def test_post_client(self):
        url = reverse('client-list')

        health_problems = [
            {'name':'diabetes', 'degree': 1},
            {'name':'diabetes', 'degree': 2},
            {'name':'parkinson', 'degree': 2},
        ]

        data = {
            'name': 'Fulano',
            'birthdate': date(2000, 5, 3),
            'gender': 'M',
            'health_problems': health_problems
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Fulano')
        self.assertEqual(Client.objects.get().health_problems.count(), 3)

class ScoreTests(SimpleTestCase):

    def test_calculate_without_health_problems(self):
        score = calculate_score_from_health_problems()

        self.assertEqual(score, 5.732417589886876)

    def test_calculate_with_many_health_problems(self):
        health_problems = [
            {'name':'diabetes', 'degree': 1},
            {'name':'diabetes', 'degree': 2},
            {'name':'parkinson', 'degree': 2},
        ]

        score = calculate_score_from_health_problems(health_problems)

        self.assertEqual(score, 90.02495108803149)
        