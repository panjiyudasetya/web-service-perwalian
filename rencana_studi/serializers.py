from rest_framework.serializers import ModelSerializer

from mata_kuliah.serializers import MataKuliahSerializer
from perwalian.serializers import PerwalianSerializer
from rencana_studi.models import RencanaStudi


class RencanaStudiSerializer(ModelSerializer):
    perwalian = PerwalianSerializer()
    mata_kuliah = MataKuliahSerializer()

    class Meta:
        model = RencanaStudi
        fields = (
            'id',
            'perwalian',
            'mata_kuliah',
            'grade',
        )
