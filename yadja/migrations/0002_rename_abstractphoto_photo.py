# Generated by Django 5.0.6 on 2024-06-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yadja', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AbstractPhoto',
            new_name='Photo',
        ),
    ]