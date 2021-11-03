# Generated by Django 3.1.13 on 2021-10-25 14:40

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('common', 'Attachment')
    for row in MyModel.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_attachment_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid),
    ]