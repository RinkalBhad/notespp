# Generated by Django 4.2.6 on 2023-12-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=10)),
                ('query', models.CharField(max_length=10)),
                ('file', models.FileField(upload_to='media')),
                ('cate', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]