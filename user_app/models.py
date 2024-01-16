from django.db import models
from django.contrib.auth.hashers import make_password

class UserPengguna(models.Model):
    user_id = models.AutoField(primary_key=True)
    nama_lengkap = models.CharField(max_length=255)
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=128)  # Field untuk menyimpan kata sandi

    def save(self, *args, **kwargs):
        # Jika password tidak dihash, hash sebelum menyimpan ke database
        if not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama_lengkap