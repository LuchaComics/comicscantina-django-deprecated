from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from api.models.ec.organization import Organization
from api.models.ec.employee import Employee
from api.models.ec.store import Store
from api.models.ec.receipt import Receipt


#@login_required(login_url='/inventory/login')
def login_page(request):
    return render(request, 'mobile_pos/login.html',{
        'page':'login',
    })