from django.db import models
from django.utils.translation import gettext_lazy as _

class Recipient(models.Model):
    BLOOD_GROUPS = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    patient_name = models.CharField(_("Patient Name"), max_length=100)
    blood_group = models.CharField(_("Blood Group"), max_length=3, choices=BLOOD_GROUPS)
    hospital_name = models.CharField(_("Hospital Name"), max_length=150)
    contact_number = models.CharField(_("Contact Number"), max_length=20)
    required_date = models.DateField(_("Required Date"))
    is_fulfilled = models.BooleanField(_("Fulfilled"), default=False)

    def __str__(self):
        return f"{self.patient_name} ({self.blood_group})"
