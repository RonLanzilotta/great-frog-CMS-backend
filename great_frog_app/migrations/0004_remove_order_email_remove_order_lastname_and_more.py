# Generated by Django 4.2 on 2023-04-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_frog_app', '0003_rename_firstname_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AlterField(
            model_name='order',
            name='dateOrdered',
            field=models.DateTimeField(auto_now=True, verbose_name='date ordered'),
        ),
    ]
