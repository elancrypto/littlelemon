# Generated by Django 4.2.1 on 2023-05-31 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_alter_menu_inventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="No_of_guests",
            field=models.SmallIntegerField(),
        ),
    ]