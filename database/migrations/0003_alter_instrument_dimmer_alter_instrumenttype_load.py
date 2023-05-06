# Generated by Django 4.1.2 on 2023-05-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_gobo_gobocode_alter_gobo_goboname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='dimmer',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='instrumenttype',
            name='load',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
