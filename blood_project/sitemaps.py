from django.contrib.sitemaps import Sitemap
from donors.models import Donor
from recipients.models import Recipient

class DonorSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Donor.objects.all()

    def lastmod(self, obj):
        return obj.date_registered

class RecipientSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Recipient.objects.all()

    def lastmod(self, obj):
        return obj.date_registered
