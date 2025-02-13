from netbox.plugins import PluginConfig

class AssetManagementConfig(PluginConfig):
    name = 'netbox_asset_management'
    verbose_name = 'Asset Management'
    description = 'Extends NetBox with asset lifecycle management features'
    version = '0.1'
    author = 'Eric Hester'
    author_email = 'hester1@clemson.edu'
    base_url = 'asset-management'
    required_settings = []
    default_settings = {}

config = AssetManagementConfig