from .models import Dealer
from rest_framework import viewsets, permissions, mixins
from .serializers import DealerSerializer
from rest_framework.response import Response
from rest_framework import status
class DealaerViewSet(viewsets.ModelViewSet, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Dealer.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DealerSerializer


