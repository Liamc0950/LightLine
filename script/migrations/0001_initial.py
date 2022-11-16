# Generated by Django 4.1.2 on 2022-11-14 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('scriptName', models.CharField(max_length=128, unique=True)),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('active', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'ordering': ['scriptName'],
            },
        ),
    ]