# Generated by Django 3.2.16 on 2022-10-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
