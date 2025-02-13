from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_asset_management:purchaseorder_list',
        link_text='Purchase Orders',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_asset_management:purchaseorder_create',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_asset_management.add_purchaseorder'],
            ),
            PluginMenuButton(
                link='plugins:netbox_asset_management:purchaseorder_bulk_import',
                title='Import',
                icon_class='mdi mdi-file-import',
                permissions=['netbox_asset_management.add_purchaseorder'],
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_asset_management:license_list',
        link_text='Licenses',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_asset_management:license_create',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_asset_management.add_license'],
            ),
            PluginMenuButton(
                link='plugins:netbox_asset_management:license_bulk_import',
                title='Import',
                icon_class='mdi mdi-file-import',
                permissions=['netbox_asset_management.add_license'],
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_asset_management:supportcontract_list',
        link_text='Support Contracts',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_asset_management:supportcontract_create',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_asset_management.add_supportcontract'],
            ),
            PluginMenuButton(
                link='plugins:netbox_asset_management:supportcontract_bulk_import',
                title='Import',
                icon_class='mdi mdi-file-import',
                permissions=['netbox_asset_management.add_supportcontract'],
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_asset_management:asset_list',
        link_text='Assets',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_asset_management:asset_create',
                title='Add',
                icon_class='mdi mdi-plus-thick',
                permissions=['netbox_asset_management.add_assetinformation'],
            ),
            PluginMenuButton(
                link='plugins:netbox_asset_management:asset_bulk_import',
                title='Import',
                icon_class='mdi mdi-file-import',
                permissions=['netbox_asset_management.add_assetinformation'],
            ),
        )
    ),
)

menu = PluginMenu(
    label='Asset Management',
    groups=(
        ('Asset Management', menu_items), 
    ),
    icon_class='mdi mdi-package-variant-closed'
)

buttons = (
    PluginMenuButton(
        link='plugins:netbox_asset_management:purchaseorder_create',
        title='Add Purchase Order',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_asset_management.add_purchaseorder'],
    ),
    PluginMenuButton(
        link='plugins:netbox_asset_management:license_create',
        title='Add License',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_asset_management.add_license'],
    ),
    PluginMenuButton(
        link='plugins:netbox_asset_management:supportcontract_create',
        title='Add Support Contract',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_asset_management.add_supportcontract'],
    ),
    PluginMenuButton(
        link='plugins:netbox_asset_management:asset_create',
        title='Add Asset',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_asset_management.add_assetinformation'],
    ),
)