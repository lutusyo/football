from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.organizations.models import Organization
from ..serializers.organizations import OrganizationSerializer

class OrganizationViewSet(ReadOnlyModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(
            memberships__user = self.request.user,
            memberships__is_active = True,
        ).distinct()