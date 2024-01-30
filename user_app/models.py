from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import AbstractUser

        
class UserPengguna(models.Model):
    user_id = models.AutoField(primary_key=True)
    nama_lengkap = models.CharField(max_length=255)
    bio = models.TextField()
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=15)
    alamat = models.TextField()
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=128)  # Field untuk menyimpan kata sandi
    last_login = models.DateTimeField(auto_now=True)
    
    def check_password(self, raw_password):
        """
        Memeriksa kecocokan kata sandi dengan password yang tidak di-hash.
        :param raw_password: Kata sandi yang tidak di-hash
        :return: True jika kata sandi cocok, False jika tidak cocok
        """
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # Jika password tidak dihash, hash sebelum menyimpan ke database
        if not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama_lengkap