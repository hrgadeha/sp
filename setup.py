# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in smart_purchase/__init__.py
from smart_purchase import __version__ as version

setup(
	name='smart_purchase',
	version=version,
	description='App to Create Auto Purchase',
	author='SMB Solution',
	author_email='developer@smb',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
