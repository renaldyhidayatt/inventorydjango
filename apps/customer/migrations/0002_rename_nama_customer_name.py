# Generated by Django 4.0 on 2022-03-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='nama',
            new_name='name',
        ),
    ]
