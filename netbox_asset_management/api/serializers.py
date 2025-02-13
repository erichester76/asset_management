from rest_framework import serializers
from ..models import PurchaseOrder, License, SupportContract, AssetInformation

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class SupportContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportContract
        fields = '__all__'

class AssetInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetInformation
        fields = '__all__'