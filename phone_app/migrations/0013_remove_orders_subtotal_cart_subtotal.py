# Generated by Django 4.1.3 on 2022-12-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0012_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='subtotal',
        ),
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.IntegerField(null=True),
        ),
    ]
