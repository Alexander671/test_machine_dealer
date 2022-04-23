from .models import Machine
from rest_framework import viewsets, permissions
from .serializers import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MachineSerializer