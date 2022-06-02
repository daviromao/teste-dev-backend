from tabnanny import verbose
from django.db import models

class HealthProblem(models.Model):
    name = models.CharField(max_length=255)
    degree = models.PositiveSmallIntegerField(max_length=2, choices=[1, 2])

    class Meta:
       verbose_name = 'Health Problem'
       verbose_name_plural = 'Health Problems'

    def __str__(self):
        return self.name


class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Nonbinary')
    ]

    name = models.CharField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(choices=GENDER_CHOICES)
    health_problems = models.ManyToManyField(
        HealthProblem,
        related_name='health_problems',
        related_query_name='health_problems'
    )
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateField(auto_now=True)