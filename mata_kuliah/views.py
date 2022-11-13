from rest_framework.generics import ListAPIView

from mata_kuliah.serializers import MataKuliahSerializer
from mata_kuliah.models import MataKuliah


class MataKuliahListView(ListAPIView):
    serializer_class = MataKuliahSerializer
    queryset = MataKuliah.objects.all().order_by('id')
