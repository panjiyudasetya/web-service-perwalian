from django.db import models


class Dosen(models.Model):
    nid = models.CharField(max_length=8)
    nama_depan = models.CharField(max_length=152)
    nama_belakang = models.CharField(max_length=152)
    alamat = models.CharField(max_length=256)
