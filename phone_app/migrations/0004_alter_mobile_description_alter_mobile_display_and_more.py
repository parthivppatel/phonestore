# Generated by Django 4.1.3 on 2022-12-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0003_alter_mobile_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='display',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='network',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='os',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='ram',
            field=models.CharField(max_length=100, null=True),
        ),
    ]