# Generated by Django 4.0.3 on 2022-06-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0004_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='tags',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
    ]
