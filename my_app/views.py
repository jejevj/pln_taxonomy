from django.shortcuts import render,redirect,get_object_or_404
from my_app.models import *
from my_app.forms import *
from django.views.decorators.csrf import csrf_exempt
from user_app.models import *   
from my_app.decorator import *

@login_required
def home(request):
    user_id = request.session.get('user_id')
    user = UserPengguna.objects.filter(user_id=user_id).first()
    return render(request,"index.html",{'user':user})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserPengguna.objects.get(email=email)
        except UserPengguna.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            # Password cocok
            request.session['user_id'] = user.user_id # Menyimpan user_id di sesi
            request.session['nama_lengkap'] = user.nama_lengkap # Menyimpan user_id di sesi
            print("session aktif")
            return redirect('profil')  # Ganti 'home' dengan nama URL halaman setelah login
        else:
            # Tambahkan pesan kesalahan jika login gagal
            error_message = "Email atau password salah. Silakan coba lagi."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logout(request):
    # Hapus sesi user_id dari sesi
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['is_login']
    # Lakukan sesuatu setelah logout, seperti mengarahkan pengguna ke halaman login
    return redirect('login')  # Ganti 'login' dengan nama URL halaman login


# VIEWS BIDANG


def bidang(request):
    bidang_list = Bidang.objects.all()
    return render(request,"bidang.html",{'bidang_list': bidang_list})


@csrf_exempt
def tambah_bidang(request):
    if request.method == 'POST':
        form = BidangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bidang')
    else:
        form = BidangForm()
    return render(request, 'tambah_bidang.html', {'form': form})


@csrf_exempt
def edit_bidang(request):
    if request.method == 'POST':
        bidang_id = request.POST.get('bidang_id')
        bidang = Bidang.objects.get(id_bidang=bidang_id)
        form = BidangForm(request.POST, instance=bidang)
        if form.is_valid():
            form.save()
            return redirect('bidang')
    return redirect('bidang')


@csrf_exempt
def hapus_bidang(request):
    if request.method == 'POST':
        bidang_id = request.POST.get('bidang_id')
        bidang = Bidang.objects.get(id_bidang=bidang_id)
        bidang.delete()
    return redirect('bidang')



# VIEWS Jabatan


def jabatan(request):
    jabatan_list = Jabatan.objects.all()
    return render(request,"jabatan.html",{'jabatan_list': jabatan_list})


@csrf_exempt
def tambah_jabatan(request):
    if request.method == 'POST':
        form = JabatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    else:
        form = JabatanForm()
    return render(request, 'tambah_jabatan.html', {'form': form})


@csrf_exempt
def edit_jabatan(request):
    if request.method == 'POST':
        jabatan_id = request.POST.get('jabatan_id')
        jabatan = Jabatan.objects.get(id_jabatan=jabatan_id)
        form = JabatanForm(request.POST, instance=jabatan)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    return redirect('jabatan')


@csrf_exempt
def hapus_jabatan(request):
    if request.method == 'POST':
        jabatan_id = request.POST.get('jabatan_id')
        jabatan = Jabatan.objects.get(id_jabatan=jabatan_id)
        jabatan.delete()
    return redirect('jabatan')


# VIEWS Taxonomy


def taxonomy(request):
    taxonomy_list = Taxonomy.objects.all()
    return render(request, "taxonomy.html", {'taxonomy_list': taxonomy_list})
def taxonomy_pengetahuan(request):
    taxonomy_list = TaxonomyPengetahuan.objects.all()
    taxonomy_list2 = Taxonomy.objects.all()
    context = {
        'list_taxonomy':taxonomy_list,
        'taxonomy_list':taxonomy_list2
    }
    return render(request, "taxonomy_pengetahuan.html",context)

@csrf_exempt
def tambah_taxonomy_pengetahuan(request):
    if request.method == 'POST':
        form = TaxonomyPengetahuanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxonomy_pengetahuan')
    else:
        form = TaxonomyForm()
    return render(request, 'tambah_taxonomy.html', {'form': form})

@csrf_exempt
def tambah_taxonomy(request):
    if request.method == 'POST':
        form = TaxonomyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxonomy')
    else:
        form = TaxonomyForm()
    return render(request, 'tambah_taxonomy.html', {'form': form})


@csrf_exempt
def edit_taxonomy(request):
    if request.method == 'POST':
        taxonomy_id = request.POST.get('taxonomy_id')
        taxonomy = Taxonomy.objects.get(id_taxonomy=taxonomy_id)
        form = TaxonomyForm(request.POST, instance=taxonomy)
        if form.is_valid():
            form.save()
            return redirect('taxonomy')
    return redirect('taxonomy')


@csrf_exempt
def hapus_taxonomy(request):
    if request.method == 'POST':
        taxonomy_id = request.POST.get('taxonomy_id')
        taxonomy = Taxonomy.objects.get(id_taxonomy=taxonomy_id)
        taxonomy.delete()
    return redirect('taxonomy')


# CRUD Knowledge


def knowledge(request):
    knowledge_list = Knowledge.objects.all()
    for knowledge in knowledge_list:
        print(knowledge.konten_knowledge)
    return render(request,'knowledge.html',{'knowledge_list': knowledge_list})
 
   
@csrf_exempt
def tambah_knowledge(request):
    if request.method == 'POST':
        form = KnowledgeForm(request.POST, request.FILES)
            
        knowledge = form.save(commit=False)
        knowledge.konten_knowledge = request.POST.get('konten_knowledge')
        knowledge.save()
        return redirect('knowledge')

    else:
        form = KnowledgeForm()
    context = {
        'form': form,
        'bidang_list': Bidang.objects.all(),
        'jabatan_list': Jabatan.objects.all(),
        'taxonomy_list': Taxonomy.objects.all(),
        'taxonomy_pengetahuan_list': TaxonomyPengetahuan.objects.all(),
        
    }

    return render(request, 'tambah_knowledge.html', context)



@csrf_exempt
def hapus_knowledge(request, knowledge_id):
    knowledge = get_object_or_404(Knowledge, id_knowledge=knowledge_id)
    knowledge.delete()
    return redirect('knowledge')
