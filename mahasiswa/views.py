from rest_framework.generics import ListAPIView

from mahasiswa.models import Mahasiswa
from mahasiswa.serializers import MahasiswaSerialier


class MahasiswaListView(ListAPIView):
    serializer_class = MahasiswaSerialier
    queryset = Mahasiswa.objects.all().order_by('id')
