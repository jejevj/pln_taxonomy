from django.db import models

# Create your models here.
class Bidang(models.Model):
    id_bidang = models.AutoField(primary_key=True)
    nama_bidang = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_bidang