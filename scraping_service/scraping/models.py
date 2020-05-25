from django.db import models

class City(models.Model):
    """Sity in site"""

    name = models.CharField(max_leight=50, )
    slug = models.CharField(max_leight=50, blank=Trye)
        
