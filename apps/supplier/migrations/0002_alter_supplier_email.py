# Generated by Django 4.1.4 on 2022-12-07 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supplier", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="email",
            field=models.EmailField(max_length=20),
        ),
    ]
