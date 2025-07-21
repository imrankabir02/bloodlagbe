from django.contrib import admin
from .models import Donor

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'blood_group', 'area', 'phone_number', 'available', 'last_donation_date')
    list_filter = ('blood_group', 'available', 'area')
    search_fields = ('full_name', 'area')
