from rest_framework.generics import ListAPIView

from dosen.models import Dosen
from dosen.serializers import DosenSerializer


class DosenListView(ListAPIView):
    serializer_class = DosenSerializer
    queryset = Dosen.objects.all().order_by('id')
