from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class APIRootView(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users:api-root', request=request, format=format),
            # 'pages': reverse('pages:api-root', request=request, format=format), 
        })

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API Root
    path('', APIRootView.as_view(), name='api-root'),
    
    # API Apps
    path('api/v1/users/', include(('users.urls', 'users'), namespace='users')),
]
