# Generated by Django 3.2.7 on 2021-09-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idmodel',
            name='fechaexpediciondocumentopersona',
        ),
        migrations.AddField(
            model_name='idmodel',
            name='fechaexpedicioncedulapersona',
            field=models.DateTimeField(null=True),
        ),
    ]