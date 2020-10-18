#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import tesseractfield

setup(
    name='django-tesseractfield',
    version=tesseractfield.__version__,
    packages=find_packages(),
    install_requires=[
        'numpy==1.19.2',
        'opencv-python==4.4.0.44',
        'Pillow==8.0.0',
        'pytesseract==0.3.6',
    ],
    author="Dubois Romain",
    author_email="dubois.rom@gmail.com",
    description="A small app providing a tesseract field for django",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url='http://github.com/duboisR/django-tesseractfield',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Framework :: Django :: 3.1.2",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=['django', 'tesseract', 'field', 'admin'],
    requires=['django (>=2.0)'],
    license='MIT License',
)
