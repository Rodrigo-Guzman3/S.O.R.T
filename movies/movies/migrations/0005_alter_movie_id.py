# Generated by Django 4.1.8 on 2023-04-08 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20230407_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
