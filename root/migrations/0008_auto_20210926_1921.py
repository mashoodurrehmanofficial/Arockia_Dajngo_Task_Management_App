# Generated by Django 3.2.7 on 2021-09-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_initiative_table_participant_badge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='initiative_table',
            name='participant_badge',
        ),
        migrations.AddField(
            model_name='profile',
            name='participant_badges',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
    ]
