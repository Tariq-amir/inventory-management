# Generated by Django 4.0.6 on 2022-07-29 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_month_year_alter_product_alloted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='month_year',
            field=models.CharField(max_length=100),
        ),
    ]
