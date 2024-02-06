# forms.py

from django import forms
from my_app.models import *

class BidangForm(forms.ModelForm):
    class Meta:
        model = Bidang
        fields = ['nama_bidang']
        
class JabatanForm(forms.ModelForm):
    class Meta:
        model = Jabatan
        fields = ['nama_jabatan']
        
class TaxonomyForm(forms.ModelForm):
    class Meta:
        model = Taxonomy
        fields = ['nama_taxonomy']
                
class TaxonomyPengetahuanForm(forms.ModelForm):
    class Meta:
        model = TaxonomyPengetahuan
        fields = ['nama_taxonomy_pengetahuan','taxonomy']
        
class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ['judul_knowledge', 'gambar_unggulan', 'bidang', 'tipe_knowledge', 'jabatan', 'taxonomy','taxonomy_pengetahuan', 'konten_knowledge']

