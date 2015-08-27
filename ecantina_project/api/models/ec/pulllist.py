from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from api.models.ec.customer import Customer
from api.models.ec.organization import Organization
from api.models.ec.store import Store
from api.models.gcd.publisher import GCDPublisher
from api.models.gcd.series import GCDSeries

class Pulllist(models.Model):
    class Meta:
        app_label = 'api'
        ordering = ('series',)
        db_table = 'ec_pulllists'
    
    pulllist_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization)
    store = models.ForeignKey(Store)
    series = models.ForeignKey(GCDSeries, null=True)
    
    def __str__(self):
        return str(self.series)