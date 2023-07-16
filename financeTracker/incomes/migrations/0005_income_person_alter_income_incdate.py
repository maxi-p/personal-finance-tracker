# Generated by Django 4.2.2 on 2023-07-14 01:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0004_appusers_alter_income_incdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pluses', to='incomes.appusers'),
        ),
        migrations.AlterField(
            model_name='income',
            name='incDate',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 7, 14, 1, 31, 6, 476330)),
        ),
    ]