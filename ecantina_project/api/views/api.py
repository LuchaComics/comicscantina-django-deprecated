from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'carts': reverse('cart-list', request=request, format=format),
        'employees': reverse('employee-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
    })