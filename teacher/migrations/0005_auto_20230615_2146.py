# Generated by Django 3.1 on 2023-06-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20230615_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('3', 'difficult'), ('1', 'easy'), ('2', 'general')], max_length=10, verbose_name='等级'),
        ),
    ]
