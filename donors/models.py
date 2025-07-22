from django.db import models

class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('ALL', 'All Groups'),
        ('NA', 'N/A'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, default='NA', db_index=True)
    area = models.CharField(max_length=100, db_index=True)
    available = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
