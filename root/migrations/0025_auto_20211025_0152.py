# Generated by Django 3.2.8 on 2021-10-24 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0024_auto_20211025_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 1, 52, 11, 584762), null=True),
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 1, 52, 11, 584762), null=True),
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='rank',
            field=models.IntegerField(blank=True, default=10000),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 1, 52, 11, 584762), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 1, 52, 11, 584762), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 1, 52, 11, 584762), null=True),
        ),
    ]
