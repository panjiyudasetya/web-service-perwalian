from django.contrib import admin

from rencana_studi.models import RencanaStudi


class RencanaStudiAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'perwalian', 'mata_kuliah', 'grade'
    )
    list_per_page = 25
    raw_id_fields = ('perwalian', 'mata_kuliah',)


admin.site.register(RencanaStudi, RencanaStudiAdmin)
