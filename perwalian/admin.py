from django.contrib import admin

from perwalian.models import Perwalian


class PerwalianAdmin(admin.ModelAdmin):
    list_display = (
        'kode', 'mahasiswa', 'dosen', 'mulai_tahun_ajaran',
        'akhir_tahun_ajaran', 'tanggal_perwalian', 'masalah', 'saran',
    )
    list_per_page = 25
    raw_id_fields = ('mahasiswa', 'dosen',)


admin.site.register(Perwalian, PerwalianAdmin)
