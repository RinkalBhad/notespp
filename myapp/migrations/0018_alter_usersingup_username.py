# Generated by Django 4.2.6 on 2023-12-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_notes_mynotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersingup',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
