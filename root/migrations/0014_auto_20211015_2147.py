# Generated by Django 3.2.7 on 2021-10-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0013_auto_20210926_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badges_container',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='badges_container',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='initiative_table',
            name='category',
        ),
        migrations.RemoveField(
            model_name='initiative_table',
            name='enrolled',
        ),
        migrations.RemoveField(
            model_name='initiative_table',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='initiative_table',
            name='particiapnt_badges',
        ),
        migrations.DeleteModel(
            name='Badges',
        ),
        migrations.DeleteModel(
            name='Badges_Container',
        ),
        migrations.DeleteModel(
            name='Initiative_Category',
        ),
        migrations.DeleteModel(
            name='Initiative_Table',
        ),
    ]
