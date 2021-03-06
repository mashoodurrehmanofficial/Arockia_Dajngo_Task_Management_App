# Generated by Django 3.2.8 on 2021-10-24 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0026_auto_20211025_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 4, 52, 14, 219115), null=True),
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 4, 52, 14, 219115), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 4, 52, 14, 220143), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 4, 52, 14, 220143), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='duration',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 4, 52, 14, 220143), null=True),
        ),
    ]
