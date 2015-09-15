from datetime import date
from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras.widgets import Select, SelectDateWidget
from django.forms.widgets import EmailInput
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from api.models.ec.imageupload import ImageUpload
from api.models.ec.customer import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'billing_name', 'billing_street_name', 'billing_street_number', 'billing_unit_number', 'billing_city' , 'billing_province' , 'billing_country' , 'billing_postal' , 'billing_phone', 'billing_email', 'shipping_name', 'shipping_street_name', 'shipping_street_number', 'shipping_unit_number', 'shipping_city' , 'shipping_province' , 'shipping_country' , 'shipping_postal' , 'shipping_phone', 'shipping_email', 'email' , 'has_consented',
        ]
        labels = {
        
        }
        widgets = {
            'first_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter First Name'
            }),
            'last_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Last Name'
            }),
            'billing_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Full Name'
            }),
            'billing_street_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street #'
            }),
            'billing_street_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street Name'
            }),
            'billing_unit_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Unit #'
            }),
            'billing_city': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter City'
            }),
            'billing_province': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Province / State'
            }),
            'billing_country': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Country'
            }),
            'billing_postal': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Postal Code / Zip'
            }),
            'billing_phone': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Phone Number'
            }),
            'billing_email': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Valid Email'
            }),
            'shipping_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Full Name'
            }),
            'shipping_street_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street #'
            }),
            'shipping_street_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street Name'
            }),
            'shipping_unit_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Unit #'
            }),
            'shipping_city': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter City'
            }),
            'shipping_province': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Province / State'
            }),
            'shipping_country': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Country'
            }),
            'shipping_postal': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Postal Code / Zip'
            }),
            'shipping_phone': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Phone Number'
            }),
            'shipping_email': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Valid Email'
            }),
            'website': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Website URL'
            }),
            'email': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Email Address'
            }),
        }