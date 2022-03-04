# Generated by Django 4.0.3 on 2022-03-04 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('alamat', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telepon', models.CharField(max_length=10)),
            ],
        ),
    ]
