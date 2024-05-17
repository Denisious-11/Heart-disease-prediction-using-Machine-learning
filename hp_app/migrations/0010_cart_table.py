# Generated by Django 3.2 on 2022-06-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0009_product_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('Product_name', models.CharField(default='', max_length=200)),
                ('Price', models.CharField(max_length=200)),
                ('Count', models.CharField(max_length=200)),
                ('Total', models.CharField(max_length=200)),
            ],
        ),
    ]