from django_tables2 import tables, Column, DateTimeColumn, TemplateColumn
from django.utils.html import format_html
from .models import PurchaseOrder, License, SupportContract, AssetInformation
from utilities.tables import BaseTable, ToggleColumn

class PurchaseOrderTable(BaseTable):
    pk = ToggleColumn()
    po_number = tables.Column(linkify=True)
    supplier = tables.Column(linkify=True)
    purchase_date = DateTimeColumn(format='Y-m-d')
    total_cost = tables.Column()
    status = tables.Column()
    tenant = tables.Column(linkify=True)
    contact = tables.Column(linkify=True)
    notes = tables.Column()
    created = DateTimeColumn(format='Y-m-d H:i')
    last_updated = DateTimeColumn(format='Y-m-d H:i')

    class Meta(BaseTable.Meta):
        model = PurchaseOrder
        fields = ('pk', 'po_number', 'supplier', 'purchase_date', 'total_cost', 'status', 'tenant', 'contact', 'notes', 'created', 'last_updated')
        default_columns = ('pk', 'po_number', 'supplier', 'purchase_date', 'status', 'tenant', 'contact')

class LicenseTable(BaseTable):
    pk = ToggleColumn()
    license_key = tables.Column(linkify=True)
    product_name = tables.Column()
    license_type = tables.Column()
    start_date = DateTimeColumn(format='Y-m-d')
    end_date = DateTimeColumn(format='Y-m-d')
    quantity = tables.Column()
    vendor = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    contact = tables.Column(linkify=True)
    purchase_order = tables.Column(linkify=True)
    notification_before_expiry = tables.Column()
    notes = tables.Column()
    unit_cost = tables.Column()
    created = DateTimeColumn(format='Y-m-d H:i')
    last_updated = DateTimeColumn(format='Y-m-d H:i')

    class Meta(BaseTable.Meta):
        model = License
        fields = ('pk', 'license_key', 'product_name', 'license_type', 'start_date', 'end_date', 'quantity', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes', 'unit_cost', 'created', 'last_updated')
        default_columns = ('pk', 'license_key', 'product_name', 'license_type', 'start_date', 'end_date', 'quantity', 'vendor', 'tenant', 'contact')

class SupportContractTable(BaseTable):
    pk = ToggleColumn()
    contract_number = tables.Column(linkify=True)
    description = tables.Column()
    start_date = DateTimeColumn(format='Y-m-d')
    end_date = DateTimeColumn(format='Y-m-d')
    vendor = tables.Column(linkify=True)
    tenant = tables.Column(linkify=True)
    contact = tables.Column(linkify=True)
    purchase_order = tables.Column(linkify=True)
    notification_before_expiry = tables.Column()
    notes = tables.Column()
    created = DateTimeColumn(format='Y-m-d H:i')
    last_updated = DateTimeColumn(format='Y-m-d H:i')

    class Meta(BaseTable.Meta):
        model = SupportContract
        fields = ('pk', 'contract_number', 'description', 'start_date', 'end_date', 'vendor', 'tenant', 'contact', 'purchase_order', 'notification_before_expiry', 'notes', 'created', 'last_updated')
        default_columns = ('pk', 'contract_number', 'description', 'start_date', 'end_date', 'vendor', 'tenant', 'contact')

class AssetInformationTable(BaseTable):
    pk = ToggleColumn()
    content_object = Column(accessor='content_object', verbose_name='Associated Object', linkify=True)
    purchase_order = tables.Column(linkify=True)
    quantity = tables.Column()
    warranty_start = DateTimeColumn(format='Y-m-d')
    warranty_end = DateTimeColumn(format='Y-m-d')
    status = tables.Column()
    serial_number = tables.Column()
    asset_tag = tables.Column()
    location = tables.Column(linkify=True)
    unit_cost = tables.Column()
    notes = tables.Column()
    created = DateTimeColumn(format='Y-m-d H:i')
    last_updated = DateTimeColumn(format='Y-m-d H:i')

    class Meta(BaseTable.Meta):
        model = AssetInformation
        fields = ('pk', 'content_object', 'purchase_order', 'quantity', 'warranty_start', 'warranty_end', 'status', 'serial_number', 'asset_tag', 'location', 'unit_cost', 'notes', 'created', 'last_updated')
        default_columns = ('pk', 'content_object', 'purchase_order', 'quantity', 'warranty_start', 'warranty_end', 'status', 'location')
