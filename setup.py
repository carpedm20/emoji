#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Setup script for emoji
"""


from codecs import open
import os

from setuptools import setup


with open('README.rst', encoding='utf-8') as f:
    readme_content = f.read().strip()


author = email = source = version = None
with open(os.path.join('emoji', '__init__.py'), encoding='utf-8') as f:
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
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="Emoji for Python",
    keywords=['emoji'],
    extras_require={
        'dev': [
            'nose',
            'coverage',
            'coveralls'
        ]
    },
    include_package_data=True,
    license="New BSD",
    long_description=readme_content,
    packages=['emoji'],
    url=source,
    version=version,
    zip_safe=True,
)
