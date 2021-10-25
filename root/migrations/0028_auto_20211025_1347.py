# Generated by Django 3.2.8 on 2021-10-25 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0027_auto_20211025_0452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore_table',
            old_name='chores_code',
            new_name='chore_code',
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 13, 47, 42, 50326), null=True),
        ),
        migrations.AlterField(
            model_name='chore_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 13, 47, 42, 50326), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='cre_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 13, 47, 42, 51324), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 13, 47, 42, 51324), null=True),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='last_updt_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 25, 13, 47, 42, 51324), null=True),
        ),
    ]