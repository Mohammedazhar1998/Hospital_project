# Generated by Django 4.2.6 on 2023-11-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0002_medicine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='desc',
            new_name='price',
        ),
    ]