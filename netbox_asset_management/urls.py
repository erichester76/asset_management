from django.urls import path, include
from . import views
from .api import views as api_views

app_name = 'netbox_asset_management'

urlpatterns = [
    # PurchaseOrder URLs
    path('purchaseorders/', views.PurchaseOrderListView.as_view(), name='purchaseorder_list'),
    path('purchaseorders/<int:pk>/', views.PurchaseOrderDetailView.as_view(), name='purchaseorder_detail'),
    path('purchaseorders/create/', views.PurchaseOrderCreateView.as_view(), name='purchaseorder_create'),
    path('purchaseorders/<int:pk>/update/', views.PurchaseOrderUpdateView.as_view(), name='purchaseorder_update'),
    path('purchaseorders/<int:pk>/delete/', views.PurchaseOrderDeleteView.as_view(), name='purchaseorder_delete'),
    path('purchaseorders/bulk/import/', views.PurchaseOrderBulkImportView.as_view(), name='purchaseorder_bulk_import'),
    path('purchaseorders/bulk/edit/', views.PurchaseOrderBulkEditView.as_view(), name='purchaseorder_bulk_edit'),
    path('purchaseorders/bulk/delete/', views.PurchaseOrderBulkDeleteView.as_view(), name='purchaseorder_bulk_delete'),
    path('purchaseorders/<int:pk>/changelog/', views.PurchaseOrderChangelogView.as_view(), name='purchaseorder_changelog'),

    # License URLs
    path('licenses/', views.LicenseListView.as_view(), name='license_list'),
    path('licenses/<int:pk>/', views.LicenseDetailView.as_view(), name='license_detail'),
    path('licenses/create/', views.LicenseCreateView.as_view(), name='license_create'),
    path('licenses/<int:pk>/update/', views.LicenseUpdateView.as_view(), name='license_update'),
    path('licenses/<int:pk>/delete/', views.LicenseDeleteView.as_view(), name='license_delete'),
    path('licenses/bulk/import/', views.LicenseBulkImportView.as_view(), name='license_bulk_import'),
    path('licenses/bulk/edit/', views.LicenseBulkEditView.as_view(), name='license_bulk_edit'),
    path('licenses/bulk/delete/', views.LicenseBulkDeleteView.as_view(), name='license_bulk_delete'),
    path('licenses/<int:pk>/changelog/', views.LicenseChangelogView.as_view(), name='license_changelog'),

    # SupportContract URLs
    path('supportcontracts/', views.SupportContractListView.as_view(), name='supportcontract_list'),
    path('supportcontracts/<int:pk>/', views.SupportContractDetailView.as_view(), name='supportcontract_detail'),
    path('supportcontracts/create/', views.SupportContractCreateView.as_view(), name='supportcontract_create'),
    path('supportcontracts/<int:pk>/update/', views.SupportContractUpdateView.as_view(), name='supportcontract_update'),
    path('supportcontracts/<int:pk>/delete/', views.SupportContractDeleteView.as_view(), name='supportcontract_delete'),
    path('supportcontracts/bulk/import/', views.SupportContractBulkImportView.as_view(), name='supportcontract_bulk_import'),
    path('supportcontracts/bulk/edit/', views.SupportContractBulkEditView.as_view(), name='supportcontract_bulk_edit'),
    path('supportcontracts/bulk/delete/', views.SupportContractBulkDeleteView.as_view(), name='supportcontract_bulk_delete'),
    path('supportcontracts/<int:pk>/changelog/', views.SupportContractChangelogView.as_view(), name='supportcontract_changelog'),

    # AssetInformation URLs
    path('assets/', views.AssetInformationListView.as_view(), name='asset_list'),
    path('assets/<int:pk>/', views.AssetInformationDetailView.as_view(), name='asset_detail'),
    path('assets/create/', views.AssetInformationCreateView.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', views.AssetInformationUpdateView.as_view(), name='asset_update'),
    path('assets/<int:pk>/delete/', views.AssetInformationDeleteView.as_view(), name='asset_delete'),
    path('assets/bulk/import/', views.AssetInformationBulkImportView.as_view(), name='asset_bulk_import'),
    path('assets/bulk/edit/', views.AssetInformationBulkEditView.as_view(), name='asset_bulk_edit'),
    path('assets/bulk/delete/', views.AssetInformationBulkDeleteView.as_view(), name='asset_bulk_delete'),
    path('assets/<int:pk>/changelog/', views.AssetInformationChangelogView.as_view(), name='asset_changelog'),
    
    # Tabs
    path('dcim/devices/<int:pk>/asset/', DeviceAssetView.as_view(), name='device_asset'),
    path('virtualization/virtual-machines/<int:pk>/asset/', VirtualMachineAssetView.as_view(), name='virtualmachine_asset'),
    path('dcim/modules/<int:pk>/asset/', ModuleAssetView.as_view(), name='module_asset'),
    path('dcim/inventory-items/<int:pk>/asset/', InventoryItemAssetView.as_view(), name='inventoryitem_asset'),


]
