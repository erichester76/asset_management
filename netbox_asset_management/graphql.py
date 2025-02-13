import strawberry
from strawberry import auto
from strawberry.django import field
from strawberry_django import DjangoObjectType, auto as django_auto
from .models import PurchaseOrder, License, SupportContract, AssetInformation
from django.contrib.contenttypes.models import ContentType

# Define GraphQL types for each model
@strawberry_django.type(PurchaseOrder)
class PurchaseOrderType(DjangoObjectType):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

@strawberry_django.type(License)
class LicenseType(DjangoObjectType):
    class Meta:
        model = License
        fields = '__all__'

@strawberry_django.type(SupportContract)
class SupportContractType(DjangoObjectType):
    class Meta:
        model = SupportContract
        fields = '__all__'

@strawberry_django.type(AssetInformation)
class AssetInformationType(DjangoObjectType):
    class Meta:
        model = AssetInformation
        fields = '__all__'

# Define Query type
@strawberry.type
class Query:
    purchase_orders: List[PurchaseOrderType] = strawberry_django.field()
    license: LicenseType = strawberry_django.field(django_auto())
    licenses: List[LicenseType] = strawberry_django.field()
    support_contracts: List[SupportContractType] = strawberry_django.field()
    assets: List[AssetInformationType] = strawberry_django.field()

# Define Mutations if needed (example for PurchaseOrder)
@strawberry.type
class Mutation:
    @strawberry_django.mutation
    def create_purchase_order(self, po_number: str, supplier: strawberry.ID, purchase_date: str, status: str, tenant: strawberry.ID = None, contact: strawberry.ID = None, total_cost: float = None) -> PurchaseOrderType:
        purchase_order = PurchaseOrder(
            po_number=po_number,
            supplier=Manufacturer.objects.get(pk=supplier),
            purchase_date=purchase_date,
            status=status,
            tenant=Tenant.objects.get(pk=tenant) if tenant else None,
            contact=User.objects.get(pk=contact) if contact else None,
            total_cost=total_cost
        )
        purchase_order.save()
        return purchase_order

    @strawberry_django.mutation
    def update_purchase_order(self, id: auto, **kwargs) -> PurchaseOrderType:
        purchase_order = PurchaseOrder.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(purchase_order, key, value)
        purchase_order.save()
        return purchase_order

    @strawberry_django.mutation
    def delete_purchase_order(self, id: auto) -> Boolean:
        try:
            purchase_order = PurchaseOrder.objects.get(pk=id)
            purchase_order.delete()
            return True
        except PurchaseOrder.DoesNotExist:
            return False

# Create schema
schema = strawberry.Schema(query=Query, mutation=Mutation)