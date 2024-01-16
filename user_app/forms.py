from django import forms
from .models import UserPengguna

class UserPenggunaForm(forms.ModelForm):
    class Meta:
        model = UserPengguna
        fields = ['nama_lengkap', 'email', 'nomor_hp', 'alamat', 'github', 'twitter', 'linkedin', 'website', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Menampilkan input sebagai password field
        }