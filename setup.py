#!/usr/bin/env python
from os import path
from setuptools import setup

def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='django-social-metadata',
    description="django-social-metadata is a Django application that provides mixin and template to display social metadata for Facebook and Google+.",
    long_description=read("README.rst"),
    version='1.0',
    maintainer="Tomasz Wysocki",
    maintainer_email="tomasz@wysocki.info",
    install_requires=(
        'django',
    ),
    packages=[
        'social_metadata',
    ],
)
