# Generated by Django 4.2 on 2023-04-25 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('great_frog_app', '0007_alter_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='great_frog_app.customer'),
        ),
    ]
