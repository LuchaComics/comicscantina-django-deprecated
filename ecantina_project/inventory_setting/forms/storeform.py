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
from api.models.ec.store import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description', 'street_name', 'street_number', 'unit_number', 'city' , 'province' , 'country' , 'postal' , 'website' , 'email' , 'phone' , 'fax' , 'is_open_monday' , 'is_open_tuesday', 'is_open_wednesday', 'is_open_thursday', 'is_open_friday', 'is_open_saturday', 'is_open_sunday', 'monday_to', 'tuesday_to', 'wednesday_to', 'thursday_to', 'friday_to', 'saturday_to', 'sunday_to', 'monday_from', 'tuesday_from', 'wednesday_from', 'thursday_from', 'friday_from', 'saturday_from', 'sunday_from',
                  ]
        labels = {
        
        }
        widgets = {
           'name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Store Name'
            }),
            'description': Textarea(attrs={
                'class': u'form-control',
                'placeholder': u'Enter Description',
                'style':'height:100px;',
            }),
            'street_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street #'
            }),
            'street_name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Street Name'
            }),
            'unit_number': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Unit #'
            }),
            'city': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter City'
            }),
            'province': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Province / State'
            }),
            'country': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Country'
            }),
            'postal': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Postal Code / Zip'
            }),
            'website': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Website URL'
            }),
            'email': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Email Address'
            }),
            'phone': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Phone Number'
            }),
            'fax': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Fax Number'
            }),
            'facebook_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Facebook URL'
            }),
            'twitter_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Twitter URL'
            }),
            'instagram_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Instagram URL'
            }),
            'linkedin_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter LinkedIn URL'
            }),
            'github_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter GitHub URL'
            }),
            'google_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Google+ URL'
            }),
            'youtube_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter YouTube URL'
            }),
            'flickr_url': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Flicker URL'
            }),    
            'monday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'tuesday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'wednesday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'thursday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'friday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'saturday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'sunday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'monday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'tuesday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'monday_to': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'wednesday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'thursday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'friday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
            'saturday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
                }),
            'sunday_from': TextInput(attrs={
                'class': u'form-control',
                'placeholder': u''
            }),
        }