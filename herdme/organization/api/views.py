from rest_framework import viewsets
from .serializers import OrganizationSerializer
from ..models import Organization


class OrganizationViewset(viewsets.ModelViewSet):
    """
    An endpoint for organizations
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
