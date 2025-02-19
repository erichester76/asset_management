from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from netbox.models import NetBoxModel
from dcim.models import Location, Manufacturer
from tenancy.models import Tenant
from users.models import User
from dcim.choices import DeviceStatusChoices

class PurchaseOrderStatusChoices(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    APPROVED = 'approved', _('Approved')
    SUBMITTED = 'submitted', _('Submitted')
    RECEIVED = 'received', _('Received')
    DEPLOYED = 'deployed', _('Deployed')

class PurchaseOrder(NetBoxModel):
    po_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.PROTECT,
        related_name='purchase_orders'
    )
    purchase_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=PurchaseOrderStatusChoices.choices,
        default=PurchaseOrderStatusChoices.DRAFT
    )
    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='purchase_orders',
        blank=True, null=True
    )
    contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='purchase_orders',
        blank=True, null=True
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"PO #{self.po_number}"

class License(NetBoxModel):
    license_key = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=100)
    license_type = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    vendor = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.PROTECT,
        related_name='licenses',
        blank=True, null=True
    )
    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='licenses',
        blank=True, null=True
    )
    contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='licenses',
        blank=True, null=True
    )
    purchase_order = models.ForeignKey(
        to=PurchaseOrder,
        on_delete=models.CASCADE,
        related_name='licenses'
    )
    notification_before_expiry = models.PositiveIntegerField(default=30, help_text="Days before expiry to notify")
    notes = models.TextField(blank=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.product_name} - {self.license_key[:8]}..."

class SupportContract(NetBoxModel):
    contract_number = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    vendor = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.PROTECT,
        related_name='support_contracts',
        blank=True, null=True
    )
    tenant = models.ForeignKey(
        to=Tenant,
        on_delete=models.PROTECT,
        related_name='support_contracts',
        blank=True, null=True
    )
    contact = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        related_name='support_contracts',
        blank=True, null=True
    )
    purchase_order = models.ForeignKey(
        to=PurchaseOrder,
        on_delete=models.CASCADE,
        related_name='support_contracts'
    )
    notification_before_expiry = models.PositiveIntegerField(default=30, help_text="Days before expiry to notify")
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Support Contract #{self.contract_number}"

class AssetInformation(NetBoxModel):
    purchase_order = models.ForeignKey(
        to=PurchaseOrder,
        on_delete=models.CASCADE,
        related_name='assets'
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': ('device', 'virtualmachine', 'module', 'inventoryitem')},
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    warranty_start = models.DateField(blank=True, null=True)
    warranty_end = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=DeviceStatusChoices,
        default=DeviceStatusChoices.STATUS_PLANNED
    )
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    asset_tag = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(
        to=Location,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='assets'
    )
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)

    licenses = models.ManyToManyField(
        License,
        related_name='assets',
        blank=True,
        through='AssetLicense'
    )
    support_contracts = models.ManyToManyField(
        SupportContract,
        related_name='assets',
        blank=True,
        through='AssetSupportContract'
    )
    class Meta:
        verbose_name_plural = "Asset Information"
    def __str__(self):
        return f"{self.content_object} Asset Info"
    
class AssetLicense(NetBoxModel):
    asset = models.ForeignKey(AssetInformation, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('asset', 'license')
        
class AssetSupportContract(NetBoxModel):
    asset = models.ForeignKey(AssetInformation, on_delete=models.CASCADE)
    support_contract = models.ForeignKey(SupportContract, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('asset', 'support_contract')