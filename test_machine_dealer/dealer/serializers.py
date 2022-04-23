from rest_framework import serializers
from .models import Dealer

class DealerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Dealer
                fields = '__all__'
                extra_kwargs = {'name': {'required': False},'official': {'required': False},'address': {'required': False}}