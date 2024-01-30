from django.shortcuts import render,redirect
from .models import UserPengguna
from .forms import UserPenggunaForm
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from my_app.decorator import *
# Create your views here.
def depan(request):
    return render(request,'index_user.html')
@login_required
def profil(request):
    
    user_id = request.session.get('user_id')
    user = UserPengguna.objects.filter(user_id=user_id).first()
    return render(request,'user_profile.html',{"user":user})

def rekomendasi_bidang(request):
    return render(request,'rekomendasi_bidang.html')

def rekomendasi_jabatan(request):
    
    return render(request,'rekomendasi_jabatan.html')

def rekomendasi_kompetensi(request):
    return render(request,'rekomendasi_kompetensi.html')

def kompetensi(request):
    return render(request,'kompetensi.html')

def detail_kompetensi(request):
    return render(request,'detail_kompetensi.html')

def list_taxonomy(request):
    return render(request,'list_taxonomy.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserPenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserPenggunaForm()

    return render(request, 'register.html', {'form': form})
    
