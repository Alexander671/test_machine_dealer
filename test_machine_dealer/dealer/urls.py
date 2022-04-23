from rest_framework import  routers
from .api import DealaerViewSet

router = routers.DefaultRouter()
router.register('', DealaerViewSet, 'dealer')


urlpatterns = router.urls
