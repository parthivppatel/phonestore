# Generated by Django 4.1.3 on 2022-12-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0019_alter_cart_date_alter_cart_is_order_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(max_length=10, null=True),
        ),
    ]