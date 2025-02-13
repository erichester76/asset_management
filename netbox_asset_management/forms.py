from django import forms
from django.utils.translation import gettext_lazy as _
from netbox.forms import NetBoxModelForm, BulkImportForm
from utilities.forms import DynamicModelChoiceField, DynamicModelMultipleChoiceField, CommentField, MarkdownField
from .models import PurchaseOrder, License, SupportContract, AssetInformation

class PurchaseOrderForm(NetBoxModelForm):
    supplier = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_("Supplier")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_("Contact")
    )

    class Meta:
        model = PurchaseOrder
        fields = ('po_number', 'supplier', 'purchase_date', 'total_cost', 'status', 'tenant', 'contact', 'notes')

class PurchaseOrderBulkImportForm(BulkImportForm):
    supplier = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Supplier")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=False,
        label=_("Contact")
    )

    class Meta:
        model = PurchaseOrder
        fields = ('po_number', 'supplier', 'purchase_date', 'total_cost', 'status', 'tenant', 'contact', 'notes')

# License Form
class LicenseForm(NetBoxModelForm):
    vendor = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_("Vendor")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_("Contact")
    )
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        required=False,
        label=_("Purchase Order")
    )

    class Meta:
        model = License
        fields = ('license_key', 'product_name', 'license_type', 'start_date', 'end_date', 'quantity', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes', 'unit_cost')

class LicenseBulkImportForm(BulkImportForm):
    vendor = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Vendor")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=False,
        label=_("Contact")
    )
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        to_field_name='po_number',
        required=False,
        label=_("Purchase Order")
    )

    class Meta:
        model = License
        fields = ('license_key', 'product_name', 'license_type', 'start_date', 'end_date', 'quantity', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes', 'unit_cost')

# SupportContract Form
class SupportContractForm(NetBoxModelForm):
    vendor = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        label=_("Vendor")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_("Contact")
    )
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        required=False,
        label=_("Purchase Order")
    )

    class Meta:
        model = SupportContract
        fields = ('contract_number', 'description', 'start_date', 'end_date', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes')

class SupportContractBulkImportForm(BulkImportForm):
    vendor = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Vendor")
    )
    tenant = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Tenant")
    )
    contact = DynamicModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=False,
        label=_("Contact")
    )
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        to_field_name='po_number',
        required=False,
        label=_("Purchase Order")
    )

    class Meta:
        model = SupportContract
        fields = ('contract_number', 'description', 'start_date', 'end_date', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes')

# AssetInformation Form
class AssetInformationForm(NetBoxModelForm):
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        required=False,
        label=_("Purchase Order")
    )
    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['device', 'virtualmachine', 'module', 'inventoryitem']),
        label=_('Object Type')
    )
    object_id = forms.IntegerField(
        label=_('Object ID'), 
        widget=forms.HiddenInput()
    )
    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        required=False,
        label=_("Location")
    )

    class Meta:
        model = AssetInformation
        fields = ('purchase_order', 'content_type', 'object_id', 'quantity', 'warranty_start', 'warranty_end', 'status', 'serial_number', 'asset_tag', 'location', 'unit_cost', 'notes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content_object'] = forms.CharField(
            label=_("Associated Object"),
            required=False,
            widget=forms.HiddenInput()
        )

    def clean(self):
        cleaned_data = super().clean()
        content_type = cleaned_data.get('content_type')
        object_id = cleaned_data.get('object_id')
        if content_type and object_id:
            try:
                content_object = content_type.get_object_for_this_type(pk=object_id)
                cleaned_data['content_object'] = content_object
            except:
                self.add_error('object_id', _("Object does not exist for the given type and ID."))
        return cleaned_data

class AssetInformationBulkImportForm(BulkImportForm):
    purchase_order = DynamicModelChoiceField(
        queryset=PurchaseOrder.objects.all(),
        to_field_name='po_number',
        required=False,
        label=_("Purchase Order")
    )
    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['device', 'virtualmachine', 'module', 'inventoryitem']),
        label=_('Object Type')
    )
    location = DynamicModelChoiceField(
        queryset=Location.objects.all(),
        to_field_name='name',
        required=False,
        label=_("Location")
    )

    class Meta:
        model = AssetInformation
        fields = ('purchase_order', 'content_type', 'object_id', 'quantity', 'warranty_start', 'warranty_end', 'status', 'serial_number', 'asset_tag', 'location', 'unit_cost', 'notes')

    def clean(self):
        cleaned_data = super().clean()
        content_type = cleaned_data.get('content_type')
        object_id = cleaned_data.get('object_id')
        if content_type and object_id:
            try:
                content_object = content_type.get_object_for_this_type(pk=object_id)
                cleaned_data['content_object'] = content_object
            except:
                self.add_error('object_id', _("Object does not exist for the given type and ID."))
        return cleaned_data