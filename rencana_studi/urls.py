from django.urls import path

from rencana_studi.views import RencanaStudiListView

urlpatterns = [
    path('rencana-studi/', RencanaStudiListView.as_view(), name='list-rencana-studi'),
]
