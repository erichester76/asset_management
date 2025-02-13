from setuptools import setup, find_packages

import os

# Get version from version file
VERSION = {}
with open(os.path.join('netbox_asset_management', 'version.py'), as_file) as fp:
    exec(fp.read(), VERSION)

setup(
    name='netbox-asset-management',
    version=VERSION['__version__'],
    description='NetBox Plugin for Asset Management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='your-github-repo-url-here',
    author='Your Name',
    author_email='your@email.com',
    license='Apache 2.0',
    install_requires=[
        'netbox>=4.0.0',
        'django>=4.2',
        'django-tables2>=2.3.1',
        'django-filter>=23.1',
        'strawberry-graphql-django>=0.5.0',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    entry_points={
        'netbox.plugins': [
            'netbox_asset_management = netbox_asset_management',
        ],
    },
)