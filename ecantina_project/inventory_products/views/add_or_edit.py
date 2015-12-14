import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from api.models.ec.imageupload import ImageUpload
from api.models.ec.organization import Organization
from api.models.ec.store import Store
from api.models.ec.brand import Brand
from api.models.ec.employee import Employee
from api.models.ec.section import Section
from api.models.ec.comic import Comic
from api.models.ec.product import Product
from api.models.ec.category import Category
from api.models.ec.tag import Tag
from api.models.ec.catalog_item import CatalogItem
from inventory_catalog.forms import CatalogItemForm
from inventory_products.forms import IssueForm
from inventory_products.forms import ComicForm
from inventory_products.forms import ImageUploadForm
from inventory_products.forms import ProductForm


@login_required(login_url='/inventory/login')
def catalog_page(request, org_id, store_id):
    try:
        catalog_items = CatalogItem.objects.filter(organization_id=org_id,store_id=store_id)
    except CatalogItem.DoesNotExist:
        catalog_items = None
    return render(request, 'inventory_products/add_or_edit/list/view.html',{
        'org': Organization.objects.get(org_id=org_id),
        'store': Store.objects.get(store_id=store_id),
        'catalog_items': catalog_items,
        'tab':'add_catalogued_product',
        'employee': Employee.objects.get(user__id=request.user.id),
        'locations': Store.objects.filter(organization_id=org_id),
    })

@login_required(login_url='/inventory/login')
def create_product_page(request, org_id, store_id, catalog_id):
    org = Organization.objects.get(org_id=org_id)
    employee = Employee.objects.get(user__id=request.user.id)
    store = Store.objects.get(store_id=store_id)
    stores = Store.objects.filter(organization=org, is_suspended=False)
    
    try:
        catalog_item = CatalogItem.objects.get(catalog_id=catalog_id)
    except CatalogItem.DoesNotExist:
        catalog_item = None

    try:
        sections = Section.objects.filter(store=store)
    except Section.DoesNotExist:
        sections = None

    try:
        tags = Tag.objects.filter(organization=org)
    except Tag.DoesNotExist:
        tags = None
    
    product_form = ProductForm(initial={'price': 5.00,})
    if stores is not None:
        # http://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
        product_form.fields["store"].queryset = stores
    if sections is not None:
        product_form.fields["section"].queryset = sections
    
    # Render page
    return render(request, 'inventory_products/add_or_edit/create/view.html',{
        'org': org,
        'store': store,
        'catalog_item': catalog_item,
        'catalog_form': CatalogItemForm(instance=catalog_item),
        'product_form': product_form,
        'tags': tags,
        'employee': Employee.objects.get(user__id=request.user.id),
        'locations': Store.objects.filter(organization_id=org_id),
        'tab':'add_catalogued_product'
    })


@login_required(login_url='/inventory/login')
def update_product_page(request, org_id, store_id, catalog_id):
    org = Organization.objects.get(org_id=org_id)
    employee = Employee.objects.get(user__id=request.user.id)
    store = Store.objects.get(store_id=store_id)
    stores = Store.objects.filter(organization=org, is_suspended=False)
    
    try:
        catalog_item = CatalogItem.objects.get(catalog_id=catalog_id)
    except CatalogItem.DoesNotExist:
        catalog_item = None
    
    try:
        sections = Section.objects.filter(store=store)
    except Section.DoesNotExist:
        sections = None
    
    try:
        tags = Tag.objects.filter(organization=org)
    except Tag.DoesNotExist:
        tags = None
    
    #    try:
    #
    #        product_form = ProductForm(instance=comic.product)
    #    except Comic.DoesNotExist:
    product_form = ProductForm(initial={'price': 5.00,})
    
    if stores is not None:
        # http://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
        product_form.fields["store"].queryset = stores
    if sections is not None:
        product_form.fields["section"].queryset = sections
    
    # Render page
    return render(request, 'inventory_products/add_or_edit/update/view.html',{
        'org': org,
        'store': store,
        'catalog_item': catalog_item,
        'catalog_form': CatalogItemForm(instance=catalog_item),
        'product_form': product_form,
        'tags': tags,
        'employee': Employee.objects.get(user__id=request.user.id),
        'locations': Store.objects.filter(organization_id=org_id),
        'tab':'add_catalogued_product'
    })