from django.contrib import admin

from mata_kuliah.models import MataKuliah


class MataKuliahAdmin(admin.ModelAdmin):
    list_display = (
        'kode', 'dosen', 'nama', 'sks',
    )
    list_per_page = 25
    raw_id_fields = ('dosen',)


admin.site.register(MataKuliah, MataKuliahAdmin)
