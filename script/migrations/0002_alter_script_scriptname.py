# Generated by Django 4.1.2 on 2022-11-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='scriptName',
            field=models.CharField(max_length=128),
        ),
    ]
