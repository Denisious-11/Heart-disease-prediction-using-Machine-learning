# Generated by Django 3.2 on 2022-05-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0003_auto_20220524_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=250)),
                ('To', models.CharField(max_length=300)),
                ('chat', models.CharField(max_length=300)),
            ],
        ),
    ]
