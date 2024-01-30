from django.urls import path
from my_app.views import *
urlpatterns = [
    path('',home,name="home"),
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
    # CRUD BIDANG
    path('bidang',bidang,name="bidang"),
    path('tambah-bidang/', tambah_bidang, name='tambah_bidang'),
    path('edit-bidang/', edit_bidang, name='edit_bidang'),
    path('hapus-bidang/', hapus_bidang, name='hapus_bidang'),
    # CRUD JABATAN
    path('jabatan',jabatan,name="jabatan"),
    path('tambah-jabatan/', tambah_jabatan, name='tambah_jabatan'),
    path('edit-jabatan/', edit_jabatan, name='edit_jabatan'),
    path('hapus-jabatan/', hapus_jabatan, name='hapus_jabatan'),
    # CRUD TAXONOMY
    path('taxonomy',taxonomy,name="taxonomy"),
    path('tambah-taxonomy/', tambah_taxonomy, name='tambah_taxonomy'),
    path('edit-taxonomy/', edit_taxonomy, name='edit_taxonomy'),
    path('hapus-taxonomy/', hapus_taxonomy, name='hapus_taxonomy'),
    # CRUD KNOWLEDGE
    path('knowledge/', knowledge, name='knowledge'),
    path('tambah_knowledge/', tambah_knowledge, name='tambah_knowledge'),
    path('hapus_knowledge/<int:knowledge_id>/', hapus_knowledge, name='hapus_knowledge'),

    
    
]
