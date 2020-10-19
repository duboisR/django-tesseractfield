#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import tesseractfield

setup(
    name='djtesseract',
    version=tesseractfield.__version__,
    packages=find_packages(exclude=("test",)),
    install_requires=[
        'numpy==1.19.2',
        'opencv-python==4.4.0.44',
        'Pillow==8.0.0',
        'pytesseract==0.3.6',
    ],
    author="Yalim Erdem",
    author_email="yalim.erdem@gmail.com",
    description="A small app providing a tesseract field for django 3.1.2",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='https://github.com/YlmRdm/django-tesseractfield',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=['django', 'tesseract', 'field', 'admin'],
    requires=['django (>=3.0)'],
    license='MIT License',
)
