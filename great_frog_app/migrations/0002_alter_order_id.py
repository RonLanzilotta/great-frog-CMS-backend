# Generated by Django 4.2 on 2023-04-28 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_frog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]