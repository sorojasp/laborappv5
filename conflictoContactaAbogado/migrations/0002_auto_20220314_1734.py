# Generated by Django 3.2.7 on 2022-03-14 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demandaPersonaNatural', '0006_alter_demandapersonanaturalmodel_fechademandapersonanatural'),
        ('demandaEmpresa', '0005_alter_demandaempresamodel_montototaldemandapersjuri'),
        ('conflictoContactaAbogado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conflictocontactaabogadomodel',
            name='demandaEmpresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demandaEmpresa.demandaempresamodel'),
        ),
        migrations.AlterField(
            model_name='conflictocontactaabogadomodel',
            name='demandaPersonaNatural',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demandaPersonaNatural.demandapersonanaturalmodel'),
        ),
    ]