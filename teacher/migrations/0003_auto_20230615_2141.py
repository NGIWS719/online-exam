# Generated by Django 3.1 on 2023-06-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20230615_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('2', 'general'), ('3', 'difficult'), ('1', 'easy')], max_length=10, verbose_name='等级'),
        ),
    ]
