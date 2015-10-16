from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ecantina_project import constants
from api.models.ec.organization import Organization
from api.models.ec.store import Store
from api.models.ec.customer import Customer
from api.models.ec.employee import Employee
from api.models.ec.product import Product
from django.core.cache import caches


class ReceiptManager(models.Manager):
    def get_or_create_for_customer(self, customer):
        """
            Function will lookup the Receipt based off the Customer info. If
            a Receipt was not found, then this function will create one and
            return an empty Receipt assigned to this Customer.
            """
        try:
            return self.get(customer=customer)
        except Receipt.DoesNotExist:
            return self.create(
                customer=customer,
                email = customer.email,
                billing_name = customer.billing_name,
                billing_address = customer.billing_address,
                billing_phone = customer.billing_phone,
                billing_city = customer.billing_city,
                billing_province = customer.billing_province,
                billing_country = customer.billing_country,
                billing_postal = customer.billing_postal,
                shipping_name = customer.shipping_name,
                shipping_address = customer.shipping_address,
                shipping_phone = customer.shipping_phone,
                shipping_city = customer.shipping_city,
                shipping_province = customer.shipping_province,
                shipping_country = customer.shipping_country,
                shipping_postal = customer.shipping_postal,
            )


class Receipt(models.Model):
    class Meta:
        app_label = 'api'
        ordering = ('last_updated',)
        db_table = 'ec_receipts'
    
    # Meta & Data-Mining
    objects = ReceiptManager()
    organization = models.ForeignKey(Organization, null=True, blank=True, db_index=True)
    store = models.ForeignKey(Store, null=True, blank=True, db_index=True)
    employee = models.ForeignKey(Employee, null=True, blank=True, db_index=True)
    customer = models.ForeignKey(Customer, null=True, blank=True, db_index=True)
    receipt_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    last_updated = models.DateTimeField(auto_now=True)
    purchased = models.DateTimeField(null=True, blank=True, db_index=True)
    has_purchased_online = models.BooleanField(default=False)
    payment_method = models.PositiveSmallIntegerField(
        default=1,
        choices=constants.PAYMENT_METHOD_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(9)],
    )
    status = models.PositiveSmallIntegerField(
        default=1,
        choices=constants.STATUS_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        db_index=True
    )
    
    # Financial
    sub_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    has_tax = models.BooleanField(default=True)
    tax_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    tax_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    has_finished = models.BooleanField(default=False, db_index=True)
    has_paid = models.BooleanField(default=False)
    
    # Payer Information
    email = models.EmailField(null=True, blank=True)
    billing_name = models.CharField(max_length=126, null=True, blank=True)
    billing_address = models.CharField(max_length=63, null=True, blank=True)
    billing_phone = models.CharField(max_length=10, null=True, blank=True)
    billing_city = models.CharField(max_length=63, null=True, blank=True)
    billing_province = models.CharField(max_length=63, null=True, blank=True)
    billing_country = models.CharField(max_length=63, null=True, blank=True)
    billing_postal = models.CharField(max_length=31, null=True, blank=True)
    shipping_name = models.CharField(max_length=126, null=True, blank=True)
    shipping_address = models.CharField(max_length=63, null=True, blank=True)
    shipping_phone = models.CharField(max_length=10, null=True, blank=True)
    shipping_city = models.CharField(max_length=63, null=True, blank=True)
    shipping_province = models.CharField(max_length=63, null=True, blank=True)
    shipping_country = models.CharField(max_length=63, null=True, blank=True)
    shipping_postal = models.CharField(max_length=31, null=True, blank=True)

    # This variable is used to track all the "Products" that are either
    # checked out or are to be purchased (in cart).
    products = models.ManyToManyField(Product, blank=True, related_name='receipt_products')

    # Error handling
    has_error = models.BooleanField(default=False, db_index=True)
    error = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        choices=constants.RECEIPT_ERROR_CHOICES,
        default=0,
    )

    def __str__(self):
        return "Receipt #" + str(self.receipt_id) + " - " + self.billing_first_name + " " + self.billing_last_name

    def save(self, *args, **kwargs):
        """
            Override the save function to reset the cache when a save was made.
        """
        cache = caches['default']
        if cache is not None:
            cache.clear()
            super(Receipt, self).save(*args, **kwargs)