from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'purchaseorders', views.PurchaseOrderViewSet)
router.register(r'licenses', views.LicenseViewSet)
router.register(r'supportcontracts', views.SupportContractViewSet)
router.register(r'assets', views.AssetInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]