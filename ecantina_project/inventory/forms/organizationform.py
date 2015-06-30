from datetime import date
from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras.widgets import Select, SelectDateWidget
from django.forms.widgets import EmailInput
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from inventory.models.ec.imageupload import ImageUpload
from inventory.models.ec.organization import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'joined', 'street_name', 'street_number', 'unit_number', 'city' , 'province' , 'country' , 'postal' , 'website' , 'email' , 'phone' , 'fax' , 'twitter_url' , 'facebook_url' , 'instagram_url' , 'linkedin_url' , 'github_url' , 'google_url' , 'youtube_url' , 'flickr_url' , 'logo']
        labels = {
        
        }
        widgets = {
           'name': TextInput(attrs={
                'class': u'form-control mb-lg',
                'placeholder': u'Enter Organization Name'
           }),
           'description': Textarea(attrs={
                'class': u'form-control',
                'placeholder': u'Enter Description',
                'style':'height:280px;',
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
        }