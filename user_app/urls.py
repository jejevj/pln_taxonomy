from django.urls import path
from user_app.views import *

urlpatterns = [
    path('',depan,name='depan'),
    path('profil',profil,name='profil'),
    path('rekomendasi-bidang',rekomendasi_bidang,name='rekomendasi-bidang'),
    path('rekomendasi-jabatan',rekomendasi_jabatan,name='rekomendasi-jabatan'),
    path('rekomendasi-kompetensi',rekomendasi_kompetensi,name='rekomendasi-kompetensi'),
    path('list-kompetensi',kompetensi,name='list-kompetensi'),
    path('detail-kompetensi/<int:id>/', detail_kompetensi, name='detail-kompetensi'),

    path('list-taxonomy',list_taxonomy,name='list-taxonomy'),
    path('register',register,name='register'),
    path('more-kompetensi',boiler,name='boiler'),
]
