# Generated by Django 4.1.2 on 2022-10-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_projectcreator'),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worknote',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
            preserve_default=False,
        ),
    ]
