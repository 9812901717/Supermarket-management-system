# Generated by Django 3.0.8 on 2020-12-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20201218_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]