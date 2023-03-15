# Generated by Django 3.2.14 on 2022-08-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0155_order_should_refresh_prices"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="tax_exemption",
            field=models.BooleanField(default=False),
        ),
        migrations.RunSQL(
            """
            ALTER TABLE order_order ALTER COLUMN tax_exemption SET DEFAULT
            false;
            """,
            migrations.RunSQL.noop,
        ),
    ]
