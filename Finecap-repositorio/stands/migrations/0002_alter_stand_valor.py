# Generated by Django 4.2.5 on 2023-10-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stand',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor'),
        ),
    ]
