# Generated by Django 5.0.1 on 2024-02-06 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_taxonomypengetahuan'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledge',
            name='taxonomy_pengetahuan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.taxonomypengetahuan'),
        ),
    ]
