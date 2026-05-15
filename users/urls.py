from rest_framework.routers import DefaultRouter
from .views import StatusViewSet

router = DefaultRouter()
router.APIRootView.name = "Users"
router.APIRootView.__doc__ = None
router.register(r'status', StatusViewSet, basename='status')

urlpatterns = router.urls
