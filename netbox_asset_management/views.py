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
    filterset = PurchaseOrderFilterSet

class PurchaseOrderDetailView(ObjectView):
    queryset = PurchaseOrder.objects.all()

class PurchaseOrderCreateView(ObjectEditView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm

class PurchaseOrderUpdateView(ObjectEditView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm

class PurchaseOrderDeleteView(ObjectDeleteView):
    model = PurchaseOrder

class PurchaseOrderBulkImportView(BulkImportView):
    queryset = PurchaseOrder.objects.all()
    model = PurchaseOrder
    table = PurchaseOrderTable
    form = PurchaseOrderBulkImportForm
    default_return_url = 'plugins:netbox_asset_management:purchaseorder_list'

class PurchaseOrderBulkEditView(BulkEditView):
    queryset = PurchaseOrder.objects.all()
    filterset = PurchaseOrderFilterSet
    table = PurchaseOrderTable
    form = PurchaseOrderForm
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
    filterset = LicenseFilterSet

class LicenseDetailView(ObjectView):
    queryset = License.objects.all()

class LicenseCreateView(ObjectEditView):
    model = License
    form_class = LicenseForm

class LicenseUpdateView(ObjectEditView):
    model = License
    form_class = LicenseForm

class LicenseDeleteView(ObjectDeleteView):
    model = License

class LicenseBulkImportView(BulkImportView):
    queryset = License.objects.all()
    model = License
    table = LicenseTable
    form = LicenseBulkImportForm
    default_return_url = 'plugins:netbox_asset_management:license_list'

class LicenseBulkEditView(BulkEditView):
    queryset = License.objects.all()
    filterset = LicenseFilterSet
    table = LicenseTable
    form = LicenseForm
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
    filterset = SupportContractFilterSet

class SupportContractDetailView(ObjectView):
    queryset = SupportContract.objects.all()

class SupportContractCreateView(ObjectEditView):
    model = SupportContract
    form_class = SupportContractForm

class SupportContractUpdateView(ObjectEditView):
    model = SupportContract
    form_class = SupportContractForm

class SupportContractDeleteView(ObjectDeleteView):
    model = SupportContract

class SupportContractBulkImportView(BulkImportView):
    queryset = SupportContract.objects.all()
    model = SupportContract
    table = SupportContractTable
    form = SupportContractBulkImportForm
    default_return_url = 'plugins:netbox_asset_management:supportcontract_list'

class SupportContractBulkEditView(BulkEditView):
    queryset = SupportContract.objects.all()
    filterset = SupportContractFilterSet
    table = SupportContractTable
    form = SupportContractForm
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
    filterset = AssetInformationFilterSet

class AssetInformationDetailView(ObjectView):
    queryset = AssetInformation.objects.all()

class AssetInformationCreateView(ObjectEditView):
    model = AssetInformation
    form_class = AssetInformationForm

class AssetInformationUpdateView(ObjectEditView):
    model = AssetInformation
    form_class = AssetInformationForm

class AssetInformationDeleteView(ObjectDeleteView):
    model = AssetInformation

class AssetInformationBulkImportView(BulkImportView):
    queryset = AssetInformation.objects.all()
    model = AssetInformation
    table = AssetInformationTable
    form = AssetInformationBulkImportForm
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationBulkEditView(BulkEditView):
    queryset = AssetInformation.objects.all()
    filterset = AssetInformationFilterSet
    table = AssetInformationTable
    form = AssetInformationForm
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationBulkDeleteView(BulkDeleteView):
    queryset = AssetInformation.objects.all()
    filterset = AssetInformationFilterSet
    table = AssetInformationTable
    confirmation_form = ConfirmationForm
    default_return_url = 'plugins:netbox_asset_management:asset_list'

class AssetInformationChangelogView(ObjectChangeLogView):
    model = AssetInformation