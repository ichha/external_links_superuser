from setuptools import find_packages, setup

setup(
    name='external_links_superuser',
    version='1.0.0',
    description='NetBox plugin: External links menu visible only to superusers',
    author='Your Name',
    author_email='you@example.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
