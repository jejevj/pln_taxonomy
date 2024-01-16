from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from my_app.models import *
from my_app.forms import *
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

# VIEWS BIDANG
def bidang(request):
    bidang_list = Bidang.objects.all()
    return render(request,"bidang.html",{'bidang_list': bidang_list})

def tambah_bidang(request):
    if request.method == 'POST':
        form = BidangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bidang')
    else:
        form = BidangForm()
    return render(request, 'tambah_bidang.html', {'form': form})

def edit_bidang(request):
    if request.method == 'POST':
        bidang_id = request.POST.get('bidang_id')
        bidang = Bidang.objects.get(id_bidang=bidang_id)
        form = BidangForm(request.POST, instance=bidang)
        if form.is_valid():
            form.save()
            return redirect('bidang')
    return redirect('bidang')

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

def tambah_jabatan(request):
    if request.method == 'POST':
        form = JabatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    else:
        form = JabatanForm()
    return render(request, 'tambah_jabatan.html', {'form': form})

def edit_jabatan(request):
    if request.method == 'POST':
        jabatan_id = request.POST.get('jabatan_id')
        jabatan = Jabatan.objects.get(id_jabatan=jabatan_id)
        form = JabatanForm(request.POST, instance=jabatan)
        if form.is_valid():
            form.save()
            return redirect('jabatan')
    return redirect('jabatan')

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

def tambah_taxonomy(request):
    if request.method == 'POST':
        form = TaxonomyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taxonomy')
    else:
        form = TaxonomyForm()
    return render(request, 'tambah_taxonomy.html', {'form': form})

def edit_taxonomy(request):
    if request.method == 'POST':
        taxonomy_id = request.POST.get('taxonomy_id')
        taxonomy = Taxonomy.objects.get(id_taxonomy=taxonomy_id)
        form = TaxonomyForm(request.POST, instance=taxonomy)
        if form.is_valid():
            form.save()
            return redirect('taxonomy')
    return redirect('taxonomy')

def hapus_taxonomy(request):
    if request.method == 'POST':
        taxonomy_id = request.POST.get('taxonomy_id')
        taxonomy = Taxonomy.objects.get(id_taxonomy=taxonomy_id)
        taxonomy.delete()
    return redirect('taxonomy')

# CRUD Knowledge
def knowledge(request):
    knowledge_list = Knowledge.objects.all()
    return render(request,'knowledge.html',{'knowledge_list': knowledge_list})
    
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
    }

    return render(request, 'tambah_knowledge.html', context)


def hapus_knowledge(request, knowledge_id):
    knowledge = get_object_or_404(Knowledge, id_knowledge=knowledge_id)
    knowledge.delete()
    return redirect('knowledge')
