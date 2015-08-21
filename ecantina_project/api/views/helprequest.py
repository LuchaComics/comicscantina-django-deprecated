from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from api.pagination import LargeResultsSetPagination
from api.permissions import BelongsToOrganization
from api.serializers import HelpRequestSerializer
from api.models.ec.helprequest import HelpRequest
from api.models.ec.organization import Organization
from api.models.ec.employee import Employee

class HelpRequestViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows customers to be viewed or edited.
    """
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = (BelongsToOrganization, IsAuthenticated)
