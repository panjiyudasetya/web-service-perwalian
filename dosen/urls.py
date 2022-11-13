from django.urls import path

from dosen.views import DosenListView

urlpatterns = [
    path('dosen/', DosenListView.as_view(), name='list-dosen'),
]
