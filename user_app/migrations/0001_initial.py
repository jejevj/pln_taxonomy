# Generated by Django 5.0.1 on 2024-01-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPengguna',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('nomor_hp', models.CharField(max_length=15)),
                ('alamat', models.TextField()),
                ('github', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
