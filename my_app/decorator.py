from django.shortcuts import  redirect
from django.contrib import messages
from functools import wraps
from user_app.models import UserPengguna  # Sesuaikan dengan lokasi model UserPengguna

# Fungsi dekorator untuk memeriksa apakah pengguna sudah login
def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        user = UserPengguna.objects.filter(user_id=user_id).first()

        # request.session['user_id'] = user.user_id # Menyimpan user_id di sesi
        request.session['nama_lengkap'] = user.nama_lengkap # Menyimpan user_id di sesi 
        request.session['email'] = user.email # Menyimpan user_id di sesi 
        request.session['is_login'] = True # Menyimpan user_id di sesi 
        if not user:
            # Jika pengguna belum login, arahkan ke halaman login
            messages.error(request, 'Anda perlu login untuk mengakses halaman ini.')
            return redirect('login')

        # Sertakan informasi pengguna sebagai argumen ke dalam view function
        return view_func(request, *args, **kwargs)

    return _wrapped_view
