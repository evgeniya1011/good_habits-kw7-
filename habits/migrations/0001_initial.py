# Generated by Django 4.2.7 on 2023-11-19 11:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='Место')),
                ('time_start', models.TimeField(verbose_name='Ввремя начала выполнения привычки')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='Приятная привычка')),
                ('periodicity', models.CharField(choices=[('1', 'раз в день'), ('2', 'раз в 2 дня'), ('3', 'раз в 3 дня'), ('4', 'раз в 4 дня'), ('5', 'раз в 5 дней'), ('6', 'раз в 6 дней'), ('7', 'раз в 7 дней')], default='1', max_length=10, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('time_complete', models.IntegerField(default=datetime.timedelta(seconds=120), verbose_name='Время на выполнение в сек')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликована')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
