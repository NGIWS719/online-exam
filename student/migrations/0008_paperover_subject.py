# Generated by Django 3.1 on 2023-06-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20230615_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='paperover',
            name='subject',
            field=models.CharField(default='', max_length=20, verbose_name='科目'),
        ),
    ]
