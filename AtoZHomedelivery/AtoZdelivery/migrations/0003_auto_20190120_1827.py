# Generated by Django 2.0.2 on 2019-01-20 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtoZdelivery', '0002_auto_20190120_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasker',
            name='t_password',
            field=models.CharField(max_length=10),
        ),
    ]