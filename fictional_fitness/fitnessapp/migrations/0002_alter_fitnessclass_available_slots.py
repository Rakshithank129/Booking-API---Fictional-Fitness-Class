# Generated by Django 5.1 on 2025-06-07 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessclass',
            name='available_slots',
            field=models.PositiveIntegerField(),
        ),
    ]
