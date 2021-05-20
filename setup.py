#!/usr/bin/env python
"""
Setup script for binance module
"""
from setuptools import setup, find_packages

setup(name='binance',
      packages=find_packages(),
      version='0.17',
      py_modules=['binance'],
      description='Binance API wrapper',
      url='https://github.com/toshima/binance',
      author='Takaki Oshima',
      author_email='t@takakioshima.com')
