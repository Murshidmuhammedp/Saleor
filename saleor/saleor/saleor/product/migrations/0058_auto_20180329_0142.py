# Generated by Django 2.0.3 on 2018-03-29 06:42

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0045_auto_20180329_0142"),
        ("product", "0057_auto_20180403_0852"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="stock", unique_together=set()),
        migrations.RemoveField(model_name="stock", name="location"),
        migrations.RemoveField(model_name="stock", name="variant"),
        migrations.AddField(
            model_name="productvariant",
            name="cost_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="quantity",
            field=models.IntegerField(
                default=Decimal("1"),
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="quantity_allocated",
            field=models.IntegerField(
                default=Decimal("0"),
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
        migrations.DeleteModel(name="Stock"),
        migrations.DeleteModel(name="StockLocation"),
    ]