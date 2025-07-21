from django.contrib import admin
from .models import Recipient

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'blood_group', 'hospital_name', 'required_date', 'is_fulfilled')
    list_filter = ('blood_group', 'is_fulfilled', 'required_date')
    search_fields = ('patient_name', 'hospital_name')
