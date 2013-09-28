#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-sqlite',
    version='0.1',
    description='Configures your django-productline database setup to use sqlite',
    long_description=read('README.rst'),
    license='The MIT License',
    keywords='django, django-productline, sqlite',
    author='Toni Michel',
    author_email='toni.michel@schnapptack.de',
    url="https://github.com/tonimichel/djpl-sqlite",
    packages=find_packages(),
    package_dir={'sqlite': 'sqlite'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
    ]
)
