# Generated by Django 4.1.2 on 2022-11-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cueList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuelist',
            name='cueListNumber',
            field=models.FloatField(default=1),
        ),
    ]
