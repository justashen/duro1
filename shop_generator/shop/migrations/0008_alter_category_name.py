# Generated by Django 5.1.4 on 2024-12-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_category_shop_owner_alter_category_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
