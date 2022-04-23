from rest_framework import  routers
from .api import MachineViewSet

router = routers.DefaultRouter()
router.register('', MachineViewSet, 'machine')


urlpatterns = router.urls
