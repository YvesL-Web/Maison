# Generated by Django 4.1.5 on 2023-02-02 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='agent',
            new_name='seller',
        ),
    ]