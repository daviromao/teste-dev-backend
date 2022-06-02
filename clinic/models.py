from django.db import models

class HealthProblem(models.Model):
    HEALTH_DEGREE_CHOICES = [
        (1, 'degree 1'),
        (2, 'degree 2')
    ]

    name = models.CharField(max_length=255)
    degree = models.PositiveSmallIntegerField(choices=HEALTH_DEGREE_CHOICES)

    class Meta:
       verbose_name = 'Health Problem'
       verbose_name_plural = 'Health Problems'

    def __str__(self):
        return f'{self.name}, degree {self.degree}'


class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Nonbinary')
    ]

    name = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    health_problems = models.ManyToManyField(
        HealthProblem,
        related_name='health_problems',
        related_query_name='health_problems'
    )
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateField(auto_now=True)
