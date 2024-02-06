from django.shortcuts import render,redirect
from .models import UserPengguna
from .forms import UserPenggunaForm
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *
from my_app.decorator import *
from my_app.models import *
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

def kompetensi(request,id):
    taxonomy_pengetahuan = TaxonomyPengetahuan.objects.filter(taxonomy_id=id) #TODO
    context = {
        'list_taxonomy':taxonomy_pengetahuan
    }
    return render(request,'kompetensi.html',context)

def detail_kompetensi(request,id):
    knowledge = Knowledge.objects.get(id_knowledge=id)
    url_gambar= str(knowledge.gambar_unggulan)
    url_gambar= url_gambar.replace('mystaticfiles/', '')
        
    context ={
        'k':knowledge,
        'url_gambar':url_gambar
        
    }
    return render(request,'detail_kompetensi.html',context)

def list_taxonomy(request):
    taxonomy = Taxonomy.objects.all()
    context = {
        'list_taxonomy':taxonomy
    }
    return render(request,'list_taxonomy.html',context)
def boiler(request,id,id2):
    list_kompetensi = Knowledge.objects.filter(taxonomy_pengetahuan_id=id2)
    taxonomy_pengetahuan = TaxonomyPengetahuan.objects.get(id_taxonomy_pengetahuan=id)
    context = {
        'list_kompetensi':list_kompetensi,
        'tax_p' : taxonomy_pengetahuan
    }
    return render(request,'boiler3.html',context)

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
    
def search(request):
    if request.method == 'GET':
        pencarian = request.GET.get('pencarian', '')
        list_knowledge = Knowledge.objects.filter(judul_knowledge__icontains=pencarian)
        for k in list_knowledge:
            k.url_gambar = str(k.gambar_unggulan)
            k.url_gambar = k.url_gambar.replace('mystaticfiles/','')
            print(k.url_gambar)
        context = {
            'knowledge':list_knowledge,
            'pencarian':pencarian
        }
        
    return render(request,'search.html',context)