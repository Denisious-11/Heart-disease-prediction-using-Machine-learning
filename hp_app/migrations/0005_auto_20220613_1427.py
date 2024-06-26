# Generated by Django 3.2 on 2022-06-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0004_chat_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
