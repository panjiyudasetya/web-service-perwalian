from django.contrib import admin

from dosen.models import Dosen


class DosenAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nid', 'nama_depan', 'nama_belakang', 'alamat',
    )
    list_per_page = 25


admin.site.register(Dosen, DosenAdmin)
