# Generated by Django 4.1.4 on 2023-01-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_tag_remove_note_type_note_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='notes.tag'),
        ),
    ]