# Generated by Django 4.0.2 on 2023-01-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Starters', 'Starters'), ('Snacks', 'Snacks'), ('Severages', 'Beverages'), ('Burgers', 'Burgers'), ('Fries', 'Fries')], max_length=200, null=True),
        ),
    ]
