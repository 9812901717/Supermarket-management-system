# Generated by Django 3.0.7 on 2020-06-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200630_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('KILOGRAM', 'kg'), ('LITRE', 'litre'), ('PACKET', 'pcs'), ('SQUAREMATER', 'm2'), ('CUBEMETER', 'm3'), ('MILLIMETRE', 'ml')], default='Choose Unit', max_length=50),
        ),
    ]