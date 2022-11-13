from rest_framework.serializers import ModelSerializer

from dosen.serializers import DosenSerializer
from mahasiswa.serializers import MahasiswaSerialier
from perwalian.models import Perwalian


class PerwalianSerializer(ModelSerializer):
    mahasiswa = MahasiswaSerialier()
    dosen = DosenSerializer()

    class Meta:
        model = Perwalian
        fields = (
            'id',
            'kode',
            'mahasiswa',
            'dosen',
            'mulai_tahun_ajaran',
            'akhir_tahun_ajaran',
            'tanggal_perwalian',
            'masalah',
            'saran',
        )
