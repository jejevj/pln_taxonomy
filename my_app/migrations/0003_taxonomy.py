# Generated by Django 5.0.1 on 2024-01-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_jabatan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id_taxonomy', models.AutoField(primary_key=True, serialize=False)),
                ('nama_taxonomy', models.CharField(max_length=255)),
            ],
        ),
    ]
