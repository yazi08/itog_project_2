from django.contrib import admin
from .models import *

# admin.site.register(Blog)
# admin.site.register(IdPid)


class HistoryClientAdmin(admin.ModelAdmin):
    list_display = ('date','data_end','summ_history_client','who')
    search_fields = ('date','who','summ_history_client')


class SummClientAdmin(admin.ModelAdmin):
    list_display = ('who_client','sum_client','date_client')

admin.site.register(HistoryClient,HistoryClientAdmin)
admin.site.register(SummClientItog,SummClientAdmin)
admin.site.register(Blog)
admin.site.register(IdPid)