# Generated by Django 3.1.14 on 2022-03-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authent', '0008_merge_20220127_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='extended_username',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Extended username'),
        ),
    ]
