# Generated by Django 3.2.7 on 2022-03-11 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contratoLaboral', '0003_contratolaboralmodel_is_active'),
        ('conflictoDespidoSJC', '0004_auto_20220310_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conflictodespidosjcmodel',
            name='contrato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contratoLaboral.contratolaboralmodel'),
        ),
    ]
