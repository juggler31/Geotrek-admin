# Generated by Django 2.0.13 on 2020-04-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200228_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='topology',
            name='geom_need_update',
            field=models.BooleanField(default=False),
        ),
    ]