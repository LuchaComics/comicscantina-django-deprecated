from django.forms import widgets
from rest_framework import serializers
from api.models.ec.cart import Cart
from api.models.ec.customer import Customer
from api.models.ec.store import Store
from api.models.ec.organization import Organization
from api.models.ec.product import Product
from api.models.ec.employee import Employee
from api.models.ec.comic import Comic
from api.models.ec.receipt import Receipt


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'joined', 'last_updated', 'first_name', 'last_name', 'email', 'phone', 'street_name', 'street_number', 'unit_number', 'province', 'country', 'postal', 'has_consented', 'user', 'profile',)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('customer', 'employee', 'products', 'cart_id', 'created', 'last_updated', 'is_closed','has_tax',)


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store_id', 'name', 'description', 'joined', 'last_updated', 'street_name', 'street_number', 'unit_number', 'city', 'province', 'country', 'postal', 'website', 'email', 'phone', 'fax', 'is_open_monday', 'is_open_tuesday', 'is_open_wednesday', 'is_open_thursday', 'is_open_friday', 'is_open_saturday', 'is_open_sunday', 'monday_to', 'tuesday_to', 'wednesday_to', 'thursday_to', 'friday_to', 'saturday_to', 'sunday_to', 'monday_from', 'tuesday_from', 'wednesday_from', 'thursday_from', 'friday_from', 'saturday_from', 'sunday_from', 'organization', 'employees', 'logo',)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('org_id', 'name', 'description', 'joined', 'last_updated', 'street_name', 'street_number', 'unit_number', 'city', 'province', 'website', 'email', 'phone', 'fax', 'twitter_url', 'facebook_url', 'instagram_url', 'linkedin_url', 'github_url', 'google_url', 'youtube_url', 'flickr_url', 'administrator', 'logo','customers',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'type', 'created', 'last_updated', 'is_sold', 'sub_price', 'discount', 'discount_type', 'price', 'cost', 'image', 'images', 'organization', 'store', 'section',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_id', 'role',  'joined', 'last_updated', 'email', 'phone', 'street_name', 'street_number', 'unit_number', 'province', 'country', 'postal', 'user', 'organization', 'profile',)


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ('comic_id', 'is_cgc_rated', 'age',
                  'cgc_rating', 'label_colour', 'condition_rating', 'is_canadian_priced_variant', 'is_variant_cover', 'is_retail_incentive_variant', 'is_newsstand_edition', 'issue',
                  )


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('organization','store','customer','receipt_id','purchased_date','type','payment_method','products','sub_total','tax_amount','total_amount',)

