# Generated by Django 4.2.6 on 2023-12-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_delete_notestb'),
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('query', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to='media')),
                ('cate', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]