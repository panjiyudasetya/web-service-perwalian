from django.contrib import admin

from mahasiswa.models import Mahasiswa


class MahasiswaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nim', 'nama_depan', 'nama_belakang',
        'alamat', 'tanggal_lahir', 'angkatan'
    )
    list_per_page = 25


admin.site.register(Mahasiswa, MahasiswaAdmin)
