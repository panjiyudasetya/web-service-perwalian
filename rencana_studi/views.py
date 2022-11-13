from rest_framework.generics import ListAPIView

from rencana_studi.serializers import RencanaStudiSerializer
from rencana_studi.models import RencanaStudi

class RencanaStudiListView(ListAPIView):
    serializer_class = RencanaStudiSerializer
    queryset = RencanaStudi.objects.all().order_by('id')
