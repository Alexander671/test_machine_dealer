from rest_framework import serializers
from .models import Machine

class MachineSerializer(serializers.ModelSerializer):
        class Meta:
                model = Machine
                fields = '__all__'
                extra_kwargs = {'machine_model': {'required': False},'date_of_create': {'required': False},'dealer': {'required': False}, 'price': {'required': False},}