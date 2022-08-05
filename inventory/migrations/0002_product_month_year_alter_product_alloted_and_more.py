# Generated by Django 4.0.6 on 2022-07-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='month_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='alloted',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='room',
            field=models.CharField(max_length=50),
        ),
    ]
