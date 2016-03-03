#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages

import cherry

setup(name='cherry',
      version=cherry.__version__,
      packages=find_packages(),

      install_requires=['poppy-creature >= 1.6.0',
                        'pypot >= 2.7.0'],

      setup_requires=['setuptools_git >= 0.3', ],

      include_package_data=True,
      exclude_package_data={'': ['README', '.gitignore']},

      zip_safe=False,

      author='Thomas',
      author_email='test@gmail.com',
      description='Cherry Software Library',
      url='https://github.com/bla.com',
      license='GNU GENERAL PUBLIC LICENSE Version 3',

      )
