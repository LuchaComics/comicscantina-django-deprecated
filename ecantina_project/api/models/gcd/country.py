from django.db import models


class Country(models.Model):
    class Meta:
        app_label = 'api'
        ordering = ('name',)
        db_table = 'gcd_countries'
    
    country_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name