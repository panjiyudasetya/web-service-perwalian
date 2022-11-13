from django.urls import path

from mahasiswa.views import MahasiswaListView

urlpatterns = [
    path('mahasiswa/', MahasiswaListView.as_view(), name='list-mahasiswa'),
]
