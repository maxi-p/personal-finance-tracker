# Generated by Django 4.2.2 on 2023-07-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incomes', '0013_alter_income_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='updates_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='updates_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]