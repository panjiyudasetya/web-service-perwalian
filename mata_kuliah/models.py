from django.db import models

from dosen.models import Dosen


class MataKuliah(models.Model):
    kode = models.CharField(max_length=8)
    dosen = models.ForeignKey(
        Dosen,
        on_delete=models.CASCADE
    )
    nama = models.CharField(max_length=152)
    sks = models.PositiveIntegerField()
