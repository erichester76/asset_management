# Asset Management Plugin for NetBox

This is the Asset Management plugin for NetBox, designed to help you manage and track your assets within the NetBox environment.

## Features

- Track hardware assets
- Manage asset lifecycle
- Integration with NetBox inventory

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/erichester76/asset-management.git
    ```
2. Install the plugin:
    ```sh
    cd netbox-asset-management
    pip install .
    ```
3. Enable the plugin in your `configuration.py`:
    ```python
    PLUGINS = ['netbox_asset_management']
    ```

4. Run database migrations:
    ```sh
    python3 manage.py migrate
    ```

## Usage

After installation, you can access the Asset Management plugin from the NetBox interface. Navigate to the Asset Management section to start managing your assets.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

---