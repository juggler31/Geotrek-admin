# Generated by Django 3.2.15 on 2022-10-04 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0035_auto_20221003_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristicevent',
            name='participant_number',
        ),
    ]
