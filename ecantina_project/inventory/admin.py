from django.contrib import admin

# Grand Comics Database Models
#------------------------------------------------------------------
from inventory.models.gcd.country import Country
from inventory.models.gcd.language import Language
from inventory.models.gcd.image import Image
from inventory.models.gcd.indiciapublisher import IndiciaPublisher
from inventory.models.gcd.publisher import Publisher
from inventory.models.gcd.brandgroup import BrandGroup
from inventory.models.gcd.brand import Brand
from inventory.models.gcd.series import Series
from inventory.models.gcd.issue import Issue
from inventory.models.gcd.storytype import StoryType
from inventory.models.gcd.story import Story
from inventory.models.gcd.branduse import BrandUse
from inventory.models.gcd.brandemblemgroup import BrandEmblemGroup

# Comics Cantina Database Models
#------------------------------------------------------------------
from inventory.models.ec.comic import Comic
from inventory.models.ec.customer import Customer
from inventory.models.ec.employee import Employee
from inventory.models.ec.helprequest import HelpRequest
from inventory.models.ec.imageupload import ImageUpload
from inventory.models.ec.organization import Organization
from inventory.models.ec.section import Section
from inventory.models.ec.store import Store


# Registering Models
#------------------------------------------------------------------
# GCD
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Image)
admin.site.register(IndiciaPublisher)
admin.site.register(BrandGroup)
admin.site.register(Brand)
admin.site.register(Series)
admin.site.register(Issue)
admin.site.register(StoryType)
admin.site.register(Story)
admin.site.register(BrandUse)
admin.site.register(BrandEmblemGroup)
# EC
admin.site.register(Comic)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(HelpRequest)
admin.site.register(ImageUpload)
admin.site.register(Organization)
admin.site.register(Section)
admin.site.register(Store)
