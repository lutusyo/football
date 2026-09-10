from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        memberships = request.user.memberships.select_related("organization")
        return Response({
            "id": request.user.id,
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "organizations": [{
                "id": m.organization.id,
                "name": m.organization.name,
                "role": m.role,
                }
                for m in memberships
                if m.is_active
            ],
        })
    