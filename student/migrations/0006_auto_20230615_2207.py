# Generated by Django 3.1 on 2023-06-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20230615_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperover',
            name='data',
            field=models.CharField(default='1', max_length=255, verbose_name='考试内容'),
        ),
    ]
