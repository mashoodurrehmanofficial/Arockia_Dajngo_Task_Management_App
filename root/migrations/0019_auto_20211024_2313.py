# Generated by Django 3.2.8 on 2021-10-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0018_auto_20211024_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chore_table',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='chore_icons/'),
        ),
        migrations.AlterField(
            model_name='transaction_table',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
