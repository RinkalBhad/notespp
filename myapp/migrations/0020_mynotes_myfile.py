# Generated by Django 4.2.6 on 2023-12-23 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_mynotes_myfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynotes',
            name='myfile',
            field=models.FileField(default=django.utils.timezone.now, upload_to='Media'),
            preserve_default=False,
        ),
    ]
