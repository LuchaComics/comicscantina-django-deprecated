from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from api.permissions import IsEmployeeUser
from api.serializers import ImageUploadSerializer
from api.models.ec.helprequest import HelpRequest
from api.models.ec.organization import Organization
from api.models.ec.employee import Employee
from api.models.ec.imageupload import ImageUpload


class ImageUploadViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows customers to be viewed or edited.
    """
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
    permission_classes = (IsEmployeeUser, IsAuthenticated)
