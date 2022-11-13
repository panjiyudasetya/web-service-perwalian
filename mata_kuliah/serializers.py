from rest_framework.serializers import ModelSerializer

from dosen.serializers import DosenSerializer
from mata_kuliah.models import MataKuliah


class MataKuliahSerializer(ModelSerializer):
    dosen = DosenSerializer()

    class Meta:
        model = MataKuliah
        fields = (
            'id',
            'kode',
            'dosen',
            'nama',
            'sks',
        )
