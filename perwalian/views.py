from rest_framework.generics import ListAPIView

from perwalian.serializers import PerwalianSerializer
from perwalian.models import Perwalian


class PerwalianListView(ListAPIView):
    serializer_class = PerwalianSerializer
    queryset = Perwalian.objects.all()
