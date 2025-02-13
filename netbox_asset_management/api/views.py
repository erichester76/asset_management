from rest_framework import viewsets
from .serializers import PurchaseOrderSerializer, LicenseSerializer, SupportContractSerializer, AssetInformationSerializer
from ..models import PurchaseOrder, License, SupportContract, AssetInformation

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class SupportContractViewSet(viewsets.ModelViewSet):
    queryset = SupportContract.objects.all()
    serializer_class = SupportContractSerializer

class AssetInformationViewSet(viewsets.ModelViewSet):
    queryset = AssetInformation.objects.all()
    serializer_class = AssetInformationSerializer