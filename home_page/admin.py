from django.contrib import admin
from .models import *

admin.site.register(Blog)


@admin.register(HistoryClient)
class HistoryClientAdmin(admin.ModelAdmin):
    list_display = ('date','data_end','summ_history_client','who')



@admin.register(SummClientItog)
class HistoryClientAdmin(admin.ModelAdmin):
    list_display = ('who_client','sum_client','date_client')