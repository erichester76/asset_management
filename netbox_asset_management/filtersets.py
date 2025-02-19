from django.db.models import Q
from django_filters import ModelChoiceFilter, DateFilter, DateTimeFilter, MultipleChoiceFilter, CharFilter
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import ContentTypeFilter
from .models import PurchaseOrder, License, SupportContract, AssetInformation
from dcim.choices import DeviceStatusChoices
from dcim.models import Manufacturer, Location 
from tenancy.models import Tenant

class PurchaseOrderFilterSet(NetBoxModelFilterSet):
    q = CharFilter(
        method='search',
        label='Search',
    )
    supplier = ModelChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label='Supplier',
    )
    tenant = ModelChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant',
    )
    contact = ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Contact',
    )
    purchase_date = DateFilter(
        label='Purchase Date'
    )
    status = MultipleChoiceFilter(
        choices=PurchaseOrderStatusChoices.choices,
        null_value=None,
        label='Status',
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(po_number__icontains=value) | Q(supplier__name__icontains=value) | Q(contact__username__icontains=value)
        return queryset.filter(qs_filter)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'po_number', 'supplier', 'purchase_date', 'total_cost', 'status', 'tenant', 'contact']

class LicenseFilterSet(NetBoxModelFilterSet):
    q = CharFilter(
        method='search',
        label='Search',
    )
    vendor = ModelChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label='Vendor',
    )
    tenant = ModelChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant',
    )
    contact = ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Contact',
    )
    start_date = DateFilter(
        label='Start Date'
    )
    end_date = DateFilter(
        label='End Date'
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(license_key__icontains=value) | Q(product_name__icontains=value) | Q(contact__username__icontains=value)
        return queryset.filter(qs_filter)

    class Meta:
        model = License
        fields = ['id', 'license_key', 'product_name', 'license_type', 'start_date', 'end_date', 'quantity', 'vendor', 'tenant', 'contact']

class SupportContractFilterSet(NetBoxModelFilterSet):
    q = CharFilter(
        method='search',
        label='Search',
    )
    vendor = ModelChoiceFilter(
        queryset=Manufacturer.objects.all(),
        label='Vendor',
    )
    tenant = ModelChoiceFilter(
        queryset=Tenant.objects.all(),
        label='Tenant',
    )
    contact = ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Contact',
    )
    start_date = DateFilter(
        label='Start Date'
    )
    end_date = DateFilter(
        label='End Date'
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(contract_number__icontains=value) | Q(description__icontains=value) | Q(contact__username__icontains=value)
        return queryset.filter(qs_filter)

    class Meta:
        model = SupportContract
        fields = ['id', 'contract_number', 'description', 'start_date', 'end_date', 'vendor', 'tenant', 'contact']

class AssetInformationFilterSet(NetBoxModelFilterSet):
    q = CharFilter(
        method='search',
        label='Search',
    )
    purchase_order = ModelChoiceFilter(
        queryset=PurchaseOrder.objects.all(),
        label='Purchase Order',
    )
    content_type = ContentTypeFilter(
        label='Object Type',
    )
    location = ModelChoiceFilter(
        queryset=Location.objects.all(),
        label='Location',
    )
    status = MultipleChoiceFilter(
        choices=DeviceStatusChoices.choices,
        null_value=None,
        label='Status',
    )
    warranty_start = DateFilter(
        label='Warranty Start'
    )
    warranty_end = DateFilter(
        label='Warranty End'
    )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(serial_number__icontains=value) | Q(asset_tag__icontains=value)
        return queryset.filter(qs_filter)

    class Meta:
        model = AssetInformation
        fields = ['id', 'purchase_order', 'quantity', 'warranty_start', 'warranty_end', 'status', 'serial_number', 'asset_tag', 'location']