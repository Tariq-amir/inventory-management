# Generated by Django 4.0.6 on 2022-08-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_product_month_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.CharField(default='2022', max_length=10),
        ),
    ]
