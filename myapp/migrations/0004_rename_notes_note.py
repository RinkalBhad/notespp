# Generated by Django 4.2.6 on 2023-12-22 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_notes_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='notes',
            new_name='note',
        ),
    ]
