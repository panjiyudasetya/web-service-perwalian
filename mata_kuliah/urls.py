from django.urls import path

from mata_kuliah.views import MataKuliahListView

urlpatterns = [
    path('mata-kuliah/', MataKuliahListView.as_view(), name='list-mata-kuliah'),
]
