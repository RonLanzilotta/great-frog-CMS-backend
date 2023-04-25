# Generated by Django 4.2 on 2023-04-25 12:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('great_frog_app', '0016_alter_order_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='great_frog_app.customer'),
            preserve_default=False,
        ),
    ]
