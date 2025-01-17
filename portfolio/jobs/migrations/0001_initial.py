# Generated by Django 5.0.3 on 2024-03-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=1000)),
                ('skills', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
