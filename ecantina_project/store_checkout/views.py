import json
from datetime import datetime
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ecantina_project import constants
from api.models.ec.organization import Organization
from api.models.ec.store import Store
from api.models.ec.comic import Comic
from api.models.ec.customer import Customer
from api.models.ec.employee import Employee
from api.models.ec.receipt import Receipt
from api.models.ec.orgshippingpreference import OrgShippingPreference
from api.models.ec.orgshippingrate import OrgShippingRate
from inventory_base.forms.customerform import CustomerForm
from inventory_base.forms.readonlycustomerform import ReadOnlyCustomerForm


def cart_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # If user is logged in, fetch the Customer record or create one. Then
    # fetch a Receipt record or create a new one.
    customer = None
    receipt = None
    if request.user.is_authenticated():
        customer = Customer.objects.get_or_create_for_user_email(request.user.email)
        receipt = Receipt.objects.get_or_create_for_online_customer(customer)

    # Display the view with all our model information.
    return render(request, 'store_checkout/cart/view.html',{
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'org': org,
        'store': store,
        'local_css_library' : settings.STORE_CSS_LIBRARY,
        'local_js_library_header' : settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body' : settings.STORE_JS_LIBRARY_BODY,
        'page' : 'home',
    })


@login_required(login_url='/')
def checkout_shipping_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)

    # Display the view with all our model information.
    return render(request, 'store_checkout/shipping/view.html',{
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library' : settings.STORE_CSS_LIBRARY,
        'local_js_library_header' : settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body' : settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@login_required(login_url='/')
def checkout_billing_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)
    
    # Display the view with all our model information.
    return render(request, 'store_checkout/billing/view.html',{
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library': settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@login_required(login_url='/')
def checkout_shipping_method_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)
    
    # Lock out 'Shipping' option if a single product in the cart requires
    # in store pickup only.
    has_no_shipping = False
    for product in receipt.products.all():
        if product.has_no_shipping:
            has_no_shipping = True

    # Lock out 'Shipping' option if the organization does not support it.
    preference = OrgShippingPreference.objects.get_by_org_or_none(organization=org)
    if preference is not None:
        if preference.is_pickup_only:
            has_no_shipping = True

    # Display the view with all our model information.
    return render(request, 'store_checkout/shipping_method/view.html',{
        'has_no_shipping': has_no_shipping,
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library': settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@login_required(login_url='/')
def checkout_payment_method_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)

    # Display the view with all our model information.
    return render(request, 'store_checkout/payment_method/view.html',{
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library': settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@csrf_exempt
@login_required(login_url='/')
def checkout_thank_you_page(request, param1_id=0, param2_id=0, param3_id=0):
    # Adaptive URL parameter extractor.
    param1_id = int(param1_id)
    param2_id = int(param2_id)
    param3_id = int(param3_id)
    org_id = 0
    store_id = 0
    receipt_id = 0
    if param1_id > 0 and param2_id == 0 and param3_id == 0:
        receipt_id = param1_id
    elif param1_id > 0 and param2_id > 0 and param3_id == 0:
        receipt_id = param2_id
        org_id = param1_id
    elif param1_id > 0 and param2_id > 0 and param3_id > 0:
        receipt_id = param3_id
        org_id = param1_id
        store_id = param2_id
    
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)

    # Fetch OLD receipt and process it.
    old_receipt = Receipt.objects.get_or_none(receipt_id=receipt_id)

    # STEP 1: Update Customer information.
    billing_address = old_receipt.customer.billing_street_number
    billing_address += ' ' + old_receipt.customer.billing_street_name
    if old_receipt.customer.billing_unit_number:
        billing_address = old_receipt.customer.billing_unit_number + '-' + billing_address
            
    shipping_address = old_receipt.customer.shipping_street_number
    shipping_address += ' ' + old_receipt.customer.shipping_street_name
    if old_receipt.customer.shipping_unit_number:
        shipping_address = old_receipt.customer.shipping_unit_number + '-' + shipping_address
    
    old_receipt.email = old_receipt.customer.email
    old_receipt.billing_address = billing_address
    old_receipt.billing_phone = old_receipt.customer.billing_phone
    old_receipt.billing_city = old_receipt.customer.billing_city
    old_receipt.billing_province = old_receipt.customer.billing_province
    old_receipt.billing_country = old_receipt.customer.billing_country
    old_receipt.billing_postal = old_receipt.customer.billing_postal
    old_receipt.shipping_address = shipping_address
    old_receipt.shipping_phone = old_receipt.customer.shipping_phone
    old_receipt.shipping_city = old_receipt.customer.shipping_city
    old_receipt.shipping_province = old_receipt.customer.shipping_province
    old_receipt.shipping_country = old_receipt.customer.shipping_country
    old_receipt.shipping_postal = old_receipt.customer.shipping_postal
        
    # STEP 2: Finalize our receipt.
    old_receipt.purchased = datetime.today()
    old_receipt.has_finished = True
    old_receipt.status = constants.ONLINE_SALE_STATUS
    old_receipt.payment_method = constants.PAYPAL_PAYMENT_METHOD
    old_receipt.save()
        
    # STEP 3: Inform our products that they are sold out.
    for product in old_receipt.products.all():
        product.is_sold = True
        product.save()

    # Fetch Customer / Receipt
    # Note: Because our previous Receipt was set "has_finished" to true
    #       this will force a new cart to be opened / created here.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)

    # Display the view with all our model information.
    return render(request, 'store_checkout/thank_you/view.html',{
        'old_receipt': old_receipt,
        'receipt': receipt,
        'customer': customer,
        'employee': employee,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library': settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@csrf_exempt
@login_required(login_url='/')
def checkout_cancel_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)
    
    # Display the view with all our model information.
    return render(request, 'store_checkout/cancel/view.html',{
        'receipt': receipt,
        'customer': customer,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library': settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })


@login_required(login_url='/')
def checkout_order_page(request, org_id=0, store_id=0):
    # Fetch the Organization / Store.
    org = Organization.objects.get_or_none(int(org_id))
    store = Store.objects.get_or_none(int(store_id))
    employee = Employee.objects.get_for_user_id_or_none(request.user.id)
    
    # Generate our URLs & pick the payment email
    paypal_email = settings.PAYPAL_RECEIVER_EMAIL
    base_url = settings.SITE_DOMAIN_URL
    if org is not None and store is None:
        base_url += "/"+str(org.org_id)
        paypal_email = org.paypal_email
    if org is not None and store is not None:
        base_url += "/"+str(org.org_id)+"/"+str(store.store_id)
        paypal_email = store.paypal_email
    return_url = base_url+"/checkout/thank_you"
    cancel_url = base_url+"/checkout/cancel"

    # Fetch Customer / Receipt.
    customer = Customer.objects.get_or_create_for_user_email(request.user.email)
    receipt = Receipt.objects.get_or_create_for_online_customer(customer)
    
    # What you want the button to do.
    paypal_dict = {
        "business": paypal_email,
        "amount": str(receipt.total_amount),
        "item_name": "Comic Book(s) Purchase, Receipt #"+str(receipt.receipt_id),
        "invoice": str(receipt.receipt_id),
        "notify_url": "/checkout/" + reverse('paypal-ipn'),
        "return_url": return_url+"/"+str(receipt.receipt_id),
        "cancel_return": cancel_url,
        "custom": "perform_receipt_checkout",  # Custom command to correlate to some function later (optional)
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    
    # Display the view with all our model information.
    return render(request, 'store_checkout/order/view.html',{
        'paypal_form': form,
        'receipt': receipt,
        'customer': customer,
        'form': CustomerForm(instance=customer),
        'org': org,
        'store': store,
        'local_css_library' : settings.STORE_CSS_LIBRARY,
        'local_js_library_header': settings.STORE_JS_LIBRARY_HEADER,
        'local_js_library_body': settings.STORE_JS_LIBRARY_BODY,
        'page': 'home',
    })
