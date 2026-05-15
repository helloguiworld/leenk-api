from rest_framework import viewsets
from rest_framework.response import Response

class StatusViewSet(viewsets.ViewSet):
    """
    Simple ViewSet to check if the API is running correctly.
    """
    def list(self, request):
        return Response({
            "status": "online",
            "message": "Leenk API is up and running!",
            "version": "v1"
        })
