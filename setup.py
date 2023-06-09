#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = []

test_requirements = ['pytest>=3', ]

setup(
    author="Pablo Ariño and Alvaro Laguna",
    author_email='pablo.arino@alumnos.upm.es',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Assignment 2 of Big Data",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='src',
    name='src',
    packages=find_packages(include=['src', 'src.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pabloo22/association_rules',
    version='0.1.0',
    zip_safe=False,
)
