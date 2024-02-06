from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Bidang(models.Model):
    id_bidang = models.AutoField(primary_key=True)
    nama_bidang = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_bidang

# Create your models here.
class Jabatan(models.Model):
    id_jabatan = models.AutoField(primary_key=True)
    nama_jabatan = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_jabatan

class Taxonomy(models.Model):
    id_taxonomy = models.AutoField(primary_key=True)
    nama_taxonomy = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_taxonomy


class TaxonomyPengetahuan(models.Model):
    id_taxonomy_pengetahuan = models.AutoField(primary_key=True)
    nama_taxonomy_pengetahuan = models.CharField(max_length=255)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nama_taxonomy_pengetahuan


class Knowledge(models.Model):
    id_knowledge = models.AutoField(primary_key=True)
    judul_knowledge = models.CharField(max_length=255)
    gambar_unggulan = models.ImageField(upload_to='mystaticfiles/knowledge_images/', null=True, blank=True)
    bidang = models.ForeignKey(Bidang, on_delete=models.CASCADE)
    tipe_knowledge = models.CharField(choices=[('jabatan', 'By Jabatan'), ('taxonomy', 'By Taxonomy')], max_length=20)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True, blank=True)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE, null=True, blank=True)
    taxonomy_pengetahuan = models.ForeignKey(TaxonomyPengetahuan,on_delete=models.CASCADE, null=True, blank=True )
    konten_knowledge = QuillField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul_knowledge
