# Generated by Django 3.1 on 2023-06-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20230615_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('1', 'easy'), ('2', 'general'), ('3', 'difficult')], max_length=10, verbose_name='等级'),
        ),
    ]
