# Generated by Django 4.0.4 on 2022-05-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='products/image'),
        ),
    ]
