from django.contrib import messages
from django.urls import reverse_lazy
from netbox.views.generic import ObjectListView, ObjectEditView, ObjectDeleteView, ObjectView, BulkImportView, BulkEditView, BulkDeleteView, ObjectChangeLogView
from utilities.forms import ConfirmationForm
from .models import PurchaseOrder, License, SupportContract, AssetInformation
from .forms import (PurchaseOrderForm, LicenseForm, SupportContractForm, AssetInformationForm,
                    PurchaseOrderBulkImportForm, LicenseBulkImportForm, SupportContractBulkImportForm, AssetInformationBulkImportForm)
from .filtersets import PurchaseOrderFilterSet, LicenseFilterSet, SupportContractFilterSet, AssetInformationFilterSet
from .tables import PurchaseOrderTable, LicenseTable, SupportContractTable, AssetInformationTable

from dcim.models import Device, Module, InventoryItem
from virtualization.models import VirtualMachine

class BaseAssetView(ObjectView):
    template_name = 'netbox_asset_management/base_asset_tab.html'

    def get_extra_context(self, request, instance):
        context = super().get_extra_context(request, instance)
        
        # Assuming your object has an asset_info relation due to the GenericForeignKey
        try:
            asset = instance.asset_info
        except AssetInformation.DoesNotExist:
            asset = None

        context['asset'] = asset
        if asset:
            context['purchase_order'] = asset.purchase_order
            context['licenses'] = asset.licenses.all()
            context['support_contracts'] = asset.support_contracts.all()
        else:
            context['purchase_order'] = None
            context['licenses'] = []
            context['support_contracts'] = []

        return context

    def get_tabs(self, request, obj):
        tabs = super().get_tabs(request, obj)
        tabs.append({
            'name': 'asset',
            'label': 'Asset',
            'badge': None,
            'permission': None,
        })
        return tabs

class DeviceAssetView(BaseAssetView):
    queryset = Device.objects.all()

class VirtualMachineAssetView(BaseAssetView):
    queryset = VirtualMachine.objects.all()

class ModuleAssetView(BaseAssetView):
    queryset = Module.objects.all()

class InventoryItemAssetView(BaseAssetView):
    queryset = InventoryItem.objects.all()
    
# PurchaseOrder Views
class PurchaseOrderListView(ObjectListView):
    queryset = PurchaseOrder.objects.all()
    table = PurchaseOrderTable
    template_name = 'netbox_asset_management/purchaseorder_list.html'
    filterset = PurchaseOrderFilterSet

class PurchaseOrderDetailView(ObjectView):
    queryset = PurchaseOrder.objects.all()
    template_name = 'netbox_asset_management/purchaseorder_detail.html'

class PurchaseOrderCreateView(ObjectEditView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'netbox_asset_management/purchaseorder_edit.html'

class PurchaseOrderUpdateView(ObjectEditView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'netbox_asset_management/purchaseorder_edit.html'

class PurchaseOrderDeleteView(ObjectDeleteView):
    model = PurchaseOrder
    template_name = 'netbox_asset_management/purchaseorder_delete.html'

class PurchaseOrderBulkImportView(BulkImportView):
    queryset = PurchaseOrder.objects.all()
    model = PurchaseOrder
    table = PurchaseOrderTable
    form = PurchaseOrderBulkImportForm
    template_name = 'netbox_asset_management/purchaseorder_import.html'
    default_return_url = 'plugins:netbox_asset_management:purchaseorder_list'

class PurchaseOrderBulkEditView(BulkEditView):
    queryset = PurchaseOrder.objects.all()
    filterset = PurchaseOrderFilterSet
    table = PurchaseOrderTable
    form = PurchaseOrderForm
    template_name = 'netbox_asset_management/purchaseorder_bulk_edit.html'
    default_return_url = 'plugins:netbox_asset_management:purchaseorder_list'

class PurchaseOrderBulkDeleteView(BulkDeleteView):
    queryset = PurchaseOrder.objects.all()
    filterset = PurchaseOrderFilterSet
    table = PurchaseOrderTable
    confirmation_form = ConfirmationForm
    default_return_url = 'plugins:netbox_asset_management:purchaseorder_list'

class PurchaseOrderChangelogView(ObjectChangeLogView):
    model = PurchaseOrder

# License Views
class LicenseListView(ObjectListView):
    queryset = License.objects.all()
    table = LicenseTable
    template_name = 'netbox_asset_management/license_list.html'
    filterset = LicenseFilterSet

class LicenseDetailView(ObjectView):
    queryset = License.objects.all()
    template_name = 'netbox_asset_management/license_detail.html'

class LicenseCreateView(ObjectEditView):
    model = License
    form_class = LicenseForm
    template_name = 'netbox_asset_management/license_edit.html'

class LicenseUpdateView(ObjectEditView):
    model = License
    form_class = LicenseForm
    template_name = 'netbox_asset_management/license_edit.html'

class LicenseDeleteView(ObjectDeleteView):
    model = License
    template_name = 'netbox_asset_management/license_delete.html'

class LicenseBulkImportView(BulkImportView):
    queryset = License.objects.all()
    model = License
    table = LicenseTable
    form = LicenseBulkImportForm
    template_name = 'netbox_asset_management/license_import.html'
    default_return_url = 'plugins:netbox_asset_management:license_list'

class LicenseBulkEditView(BulkEditView):
    queryset = License.objects.all()
    filterset = LicenseFilterSet
    table = LicenseTable
    form = LicenseForm
    template_name = 'netbox_asset_management/license_bulk_edit.html'
    default_return_url = 'plugins:netbox_asset_management:license_list'

class LicenseBulkDeleteView(BulkDeleteView):
    queryset = License.objects.all()
    filterset = LicenseFilterSet
    table = LicenseTable
    confirmation_form = ConfirmationForm
    default_return_url = 'plugins:netbox_asset_management:license_list'

class LicenseChangelogView(ObjectChangeLogView):
    model = License

# SupportContract Views
class SupportContractListView(ObjectListView):
    queryset = SupportContract.objects.all()
    table = SupportContractTable
    template_name = 'netbox_asset_management/supportcontract_list.html'
    filterset = SupportContractFilterSet

class SupportContractDetailView(ObjectView):
    queryset = SupportContract.objects.all()
    template_name = 'netbox_asset_management/supportcontract_detail.html'

class SupportContractCreateView(ObjectEditView):
    model = SupportContract
    form_class = SupportContractForm
    template_name = 'netbox_asset_management/supportcontract_edit.html'

class SupportContractUpdateView(ObjectEditView):
    model = SupportContract
    form_class = SupportContractForm
    template_name = 'netbox_asset_management/supportcontract_edit.html'

class SupportContractDeleteView(ObjectDeleteView):
    model = SupportContract
    template_name = 'netbox_asset_management/supportcontract_delete.html'

class SupportContractBulkImportView(BulkImportView):
    queryset = SupportContract.objects.all()
    model = SupportContract
    table = SupportContractTable
    form = SupportContractBulkImportForm
    template_name = 'netbox_asset_management/supportcontract_import.html'
    default_return_url = 'plugins:netbox_asset_management:supportcontract_list'

class SupportContractBulkEditView(BulkEditView):
    queryset = SupportContract.objects.all()
    filterset = SupportContractFilterSet
    table = SupportContractTable
    form = SupportContractForm
    template_name = 'netbox_asset_management/supportcontract_bulk_edit.html'
    default_return_url = 'plugins:netbox_asset_management:supportcontract_list'

class SupportContractBulkDeleteView(BulkDeleteView):
    queryset = SupportContract.objects.all()
    filterset = SupportContractFilterSet
    table = SupportContractTable
    confirmation_form = ConfirmationForm
    default_return_url = 'plugins:netbox_asset_management:supportcontract_list'

class SupportContractChangelogView(ObjectChangeLogView):
    model = SupportContract

# AssetInformation Views
class AssetInformationListView(ObjectListView):
    queryset = AssetInformation.objects.all()
    table = AssetInformationTable
    template_name = 'netbox_asset_management/asset_list.html'
    filterset = AssetInformationFilterSet

class AssetInformationDetailView(ObjectView):
    queryset = AssetInformation.objects.all()
    template_name = 'netbox_asset_management/asset_detail.html'

class AssetInformationCreateView(ObjectEditView):
    model = AssetInformation
    form_class = AssetInformationForm
    template_name = 'netbox_asset_management/asset_edit.html'

class AssetInformationUpdateView(ObjectEditView):
    model = AssetInformation
    form_class = AssetInformationForm
    template_name = 'netbox_asset_management/asset_edit.html'

class AssetInformationDeleteView(ObjectDeleteView):
    model = AssetInformation
    template_name = 'netbox_asset_management/asset_delete.html'

class AssetInformationBulkImportView(BulkImportView):
    queryset = AssetInformation.objects.all()
    model = AssetInformation
    table = AssetInformationTable
    form = AssetInformationBulkImportForm
    template_name = 'netbox_asset_management/asset_import.html'
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationBulkEditView(BulkEditView):
    queryset = AssetInformation.objects.all()
    filterset = AssetInformationFilterSet
    table = AssetInformationTable
    form = AssetInformationForm
    template_name = 'netbox_asset_management/asset_bulk_edit.html'
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationBulkDeleteView(BulkDeleteView):
    queryset = AssetInformation.objects.all()
    filterset = AssetInformationFilterSet
    table = AssetInformationTable
    confirmation_form = ConfirmationForm
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationChangelogView(ObjectChangeLogView):
    model = AssetInformation