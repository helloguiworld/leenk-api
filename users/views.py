from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class APIStatusView(APIView):
    """
    Simple view to check if the API is running correctly.
    """
    def get(self, request):
        return Response({
            "status": "online",
            "message": "Leenk API is up and running!",
            "version": "v1"
        }, status=status.HTTP_200_OK)
