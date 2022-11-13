from django.urls import path

from perwalian.views import PerwalianListView

urlpatterns = [
    path('perwalian/', PerwalianListView.as_view(), name='list-perwalian'),
]
