# Generated by Django 3.0.5 on 2021-04-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]