# Generated by Django 5.1.3 on 2024-12-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('cid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cn', models.CharField(max_length=100)),
            ],
        ),
    ]