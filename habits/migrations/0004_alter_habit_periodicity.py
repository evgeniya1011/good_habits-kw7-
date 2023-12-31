# Generated by Django 4.2.7 on 2023-11-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(blank=True, choices=[('1', 'раз в 7 дней'), ('2', '2 раза в 7 дней'), ('3', '3 раза в 7 дней'), ('4', '4 раза в 7 дней'), ('5', '5 раз в 7 дней'), ('6', '6 раз в 7 дней'), ('7', '7 раз в 7 дней')], default=1, max_length=10, null=True, verbose_name='Периодичность:сколько раз в неделю'),
        ),
    ]
