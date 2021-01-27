# Generated by Django 3.1.5 on 2021-01-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0008_auto_20201117_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='date_insert',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Insertion date'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='date_update',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='Update date'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='publication_date',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='published',
            field=models.BooleanField(default=False, help_text='Visible on Geotrek-rando', verbose_name='Published'),
        ),
    ]