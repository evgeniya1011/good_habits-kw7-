# Generated by Django 4.2.7 on 2023-11-19 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(blank=True, choices=[('1', 'раз в день'), ('2', 'раз в 2 дня'), ('3', 'раз в 3 дня'), ('4', 'раз в 4 дня'), ('5', 'раз в 5 дней'), ('6', 'раз в 6 дней'), ('7', 'раз в 7 дней')], default='1', max_length=10, null=True, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time_complete',
            field=models.IntegerField(verbose_name='Время на выполнение в сек'),
        ),
    ]
