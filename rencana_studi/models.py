from django.db import models

from mata_kuliah.models import MataKuliah
from perwalian.models import Perwalian


class RencanaStudi(models.Model):
    perwalian = models.ForeignKey(
        Perwalian,
        on_delete=models.CASCADE
    )
    mata_kuliah = models.ForeignKey(
        MataKuliah,
        on_delete=models.CASCADE
    )
    grade = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
