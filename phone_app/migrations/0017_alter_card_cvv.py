# Generated by Django 4.1.3 on 2022-12-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0016_alter_card_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.TextField(),
        ),
    ]
