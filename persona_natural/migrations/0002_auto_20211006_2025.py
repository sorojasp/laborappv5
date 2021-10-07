# Generated by Django 3.2.7 on 2021-10-07 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_personmodel_lugarresidenciapersona'),
        ('persona_natural', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personanaturalmodel',
            name='personmodel_ptr',
        ),
        migrations.AddField(
            model_name='personanaturalmodel',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='persona.personmodel'),
        ),
    ]
