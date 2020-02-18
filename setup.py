#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import sys
import os
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Micah Johnson",
    author_email='micah.johnson150@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Launches interactive dockers",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='docker',
    name='shamu',
    packages=find_packages(include=['shamu']),
    entry_points={
        'console_scripts': [
            'shamu=shamu.launcher:main'
        ]},

    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/USDA-ARS-NWRC/shamu',
    version='0.1.3',
    zip_safe=False,
)
