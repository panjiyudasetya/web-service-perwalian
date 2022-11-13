from rest_framework.serializers import ModelSerializer

from dosen.models import Dosen


class DosenSerializer(ModelSerializer):

    class Meta:
        model = Dosen
        fields = (
            'id',
            'nid',
            'nama_depan',
            'nama_belakang',
            'alamat',
        )
