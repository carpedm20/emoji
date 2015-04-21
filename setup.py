#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Setup script for emoji
"""


import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme_content = f.read().strip()


with open('LICENSE.txt') as f:
    license_content = f.read().strip()


version = None
author = None
email = None
source = None
with open(os.path.join('emoji', '__init__.py')) as f:
    for line in f:
        if line.strip().startswith('__version__'):
            version = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__author__'):
            author = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__email__'):
            email = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif line.strip().startswith('__source__'):
            source = line.split('=')[1].strip().replace('"', '').replace("'", '')
        elif None not in (version, author, email, source):
            break

setup(
    name='emoji',
    author=author,
    author_email=email,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Emoji for Python",
    keywords=['emoji'],
    include_package_data=True,
    license=license_content,
    long_description=readme_content,
    packages=['emoji'],
    url=source,
    version=version,
    zip_safe=True,
)
