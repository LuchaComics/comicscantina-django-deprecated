import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from api.pagination import LargeResultsSetPagination
from api.permissions import BelongsToOrganizationOrCustomer
from api.models.ec.organization import Organization
from api.models.ec.employee import Employee
from api.models.ec.receipt import Receipt
from api.serializers import ReceiptSerializer


class ReceiptFilter(django_filters.FilterSet):
    has_finished = django_filters.BooleanFilter(name="has_finished")
    class Meta:
        model = Receipt
        fields = ['organization', 'store', 'customer', 'has_finished', 'status', 'has_error', 'error', 'has_purchased_online','employee',]


class ReceiptViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows customers to be viewed or edited.
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (BelongsToOrganizationOrCustomer, IsAuthenticated)
    filter_backends = (filters.SearchFilter,filters.DjangoFilterBackend,)
    search_fields = ('billing_name','email','billing_phone','billing_postal','shipping_first_name','shipping_last_name','shipping_phone','shipping_postal',)
    filter_class = ReceiptFilter