# Generated by Django 3.2.8 on 2021-10-24 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0022_auto_20211024_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 23, 59, 55, 160727), null=True),
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 23, 59, 55, 160727), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 23, 59, 55, 161724), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 23, 59, 55, 161724), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 24, 23, 59, 55, 161724), null=True),
        ),
    ]