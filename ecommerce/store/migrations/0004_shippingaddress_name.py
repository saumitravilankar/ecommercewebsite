# Generated by Django 4.1.3 on 2022-12-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_order_transaction_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="shippingaddress",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
