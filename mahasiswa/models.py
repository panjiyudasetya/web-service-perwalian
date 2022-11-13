from django.db import models


class Mahasiswa(models.Model):
    nim = models.CharField(max_length=8)
    nama_depan = models.CharField(max_length=152)
    nama_belakang = models.CharField(max_length=152)
    alamat = models.CharField(max_length=256)
    tanggal_lahir = models.DateField(null=True)
    angkatan = models.IntegerField()
