from .models import Dealer
from rest_framework import viewsets, permissions
from .serializers import DealerSerializer


class DealaerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DealerSerializer