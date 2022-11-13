from rest_framework.serializers import CharField, ModelSerializer

from mata_kuliah.serializers import MataKuliahSerializer
from rencana_studi.models import RencanaStudi


class RencanaStudiSerializer(ModelSerializer):
    kode_perwalian = CharField(source='perwalian.kode')
    mata_kuliah = MataKuliahSerializer()

    class Meta:
        model = RencanaStudi
        fields = (
            'id',
            'kode_perwalian',
            'mata_kuliah',
            'grade',
        )
