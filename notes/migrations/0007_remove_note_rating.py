# Generated by Django 4.1.4 on 2023-01-03 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_alter_note_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='rating',
        ),
    ]
