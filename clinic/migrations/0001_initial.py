# Generated by Django 4.0.5 on 2022-06-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('degree', models.PositiveSmallIntegerField(choices=[(1, 'degree 1'), (2, 'degree 2')])),
            ],
            options={
                'verbose_name': 'Health Problem',
                'verbose_name_plural': 'Health Problems',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Nonbinary')], max_length=1)),
                ('updated_at', models.DateField(auto_now=True)),
                ('health_problems', models.ManyToManyField(related_name='health_problems', related_query_name='health_problems', to='clinic.healthproblem')),
            ],
        ),
    ]
