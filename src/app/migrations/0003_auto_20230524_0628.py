# Generated by Django 3.2.18 on 2023-05-24 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230524_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licensenamespace',
            name='text',
        ),
        migrations.RemoveField(
            model_name='licenserequest',
            name='text',
        ),
    ]
