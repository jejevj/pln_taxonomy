from django.shortcuts import render
# Create your views here.
def depan(request):
    return render(request,'index_user.html')

def profil(request):
    return render(request,'user_profile.html')

def rekomendasi_bidang(request):
    return render(request,'rekomendasi_bidang.html')

def rekomendasi_jabatan(request):
    return render(request,'rekomendasi_jabatan.html')

def rekomendasi_kompetensi(request):
    return render(request,'kompetensi.html')

def detail_kompetensi(request):
    return render(request,'detail_kompetensi.html')

def list_taxonomy(request):
    return render(request,'list_taxonomy.html')
    
