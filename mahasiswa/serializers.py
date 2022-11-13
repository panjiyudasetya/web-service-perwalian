from rest_framework.serializers import ModelSerializer

from mahasiswa.models import Mahasiswa


class MahasiswaSerialier(ModelSerializer):

    class Meta:
        model = Mahasiswa
        fields = (
            'id',
            'nim',
            'nama_depan',
            'nama_belakang',
            'alamat',
            'tanggal_lahir',
            'angkatan',
        )
