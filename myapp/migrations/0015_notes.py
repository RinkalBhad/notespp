# Generated by Django 4.2.6 on 2023-12-23 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('query', models.CharField(max_length=10)),
                ('type_query', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to='media')),
                ('comment', models.TextField()),
            ],
        ),
    ]
