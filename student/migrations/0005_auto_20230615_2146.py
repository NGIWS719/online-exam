# Generated by Django 3.1 on 2023-06-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20230615_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperover',
            name='data',
            field=models.JSONField(verbose_name='考试内容'),
        ),
    ]
