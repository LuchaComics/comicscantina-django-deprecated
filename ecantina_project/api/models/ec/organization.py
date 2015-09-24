from django.db import models
from django.contrib.auth.models import User
from ecantina_project import constants
from api.models.ec.imageupload import ImageUpload
from api.models.ec.customer import Customer


class Organization(models.Model):
    class Meta:
        app_label = 'api'
        ordering = ('name',)
        db_table = 'ec_organizations'
    
    # Basic
    org_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=127)
    description = models.TextField(null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_suspended = models.BooleanField(default=False)
    
    # Location
    street_name = models.CharField(max_length=63)
    street_number = models.CharField(max_length=31, null=True, blank=True)
    unit_number = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=63)
    province = models.CharField(
        max_length=63,
        choices=constants.PROVINCE_CHOICES,
    )
    country = models.CharField(
        max_length=63,
        choices=constants.COUNTRY_CHOICES,
    )
    postal = models.CharField(max_length=31)
    currency = models.PositiveSmallIntegerField(
        default=124,
        choices=constants.ISO_4217_CURRENCY_OPTIONS,
    )
    language = models.CharField(
        max_length=2,
        choices=constants.ISO_639_1_LANGUAGE_OPTIONS,
        default='EN',
    )
    
    # Contact
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    fax = models.CharField(max_length=10, null=True, blank=True)
    
    # Social Media
    twitter_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    google_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    flickr_url = models.URLField(null=True, blank=True)

    # References
    administrator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    logo = models.ForeignKey(ImageUpload, null=True, blank=True, on_delete=models.SET_NULL)
    customers = models.ManyToManyField(Customer)
    
    def __str__(self):
        return self.name