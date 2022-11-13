from django.db import models

from dosen.models import Dosen
from mahasiswa.models import Mahasiswa


class Perwalian(models.Model):
    kode = models.CharField(max_length=12)
    mahasiswa = models.ForeignKey(
        Mahasiswa,
        on_delete=models.CASCADE,
        related_name='perwalian_as_mhs',
    )
    dosen = models.ForeignKey(
        Dosen,
        on_delete=models.CASCADE,
        related_name='perwalian_as_dosen',
    )
    mulai_tahun_ajaran = models.PositiveIntegerField()
    akhir_tahun_ajaran = models.PositiveIntegerField()
    tanggal_perwalian = models.DateField()
    masalah = models.TextField(null=True, blank=True)
    saran = models.TextField(null=True, blank=True)
