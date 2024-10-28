# Generated by Django 3.1.7 on 2021-03-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0143_rename_product_images_to_product_media"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productvariantchannellisting",
            name="price_amount",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=12, null=True
            ),
        ),
    ]