# Generated by Django 4.0.3 on 2022-06-01 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_rename_notes_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Notes',
        ),
    ]
