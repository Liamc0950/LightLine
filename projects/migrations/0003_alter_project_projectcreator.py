# Generated by Django 4.1.2 on 2022-10-25 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('projects', '0002_rename_lightingdesigner_project_projectcreator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectCreator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
