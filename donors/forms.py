from django import forms
from .models import Donor

class DateInput(forms.DateInput):
    input_type = 'date'

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['full_name', 'phone_number', 'blood_group', 'area', 'available', 'last_donation_date']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'last_donation_date': DateInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get('phone_number')
        blood_group = cleaned_data.get('blood_group')

        if phone_number and blood_group:
            # Check for the last 11 digits for uniqueness
            if len(phone_number) >= 11:
                phone_number_last_11 = phone_number[-11:]
                if Donor.objects.filter(phone_number__endswith=phone_number_last_11, blood_group=blood_group).exists():
                    raise forms.ValidationError("This donor with this phone number and blood group already exists.")
        return cleaned_data

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
