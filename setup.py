#!/usr/bin/env python

###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

REQUIREMENTS = [
  'google-api-python-client',
  'google-auth',
  'google-auth-oauthlib',
  'google-auth-httplib2',
  'google-cloud-bigquery',
  'psutil',
  'python-dateutil',
  'pytz',
]

setup(
  name='bqflow',
  version='0.0.2',
  description='BQFlow is a Google gTech built python framework for creating and sharing re-usable workflow components.',
  long_description='BQFlow is a Google gTech built python framework for creating and sharing re-usable workflow components. To make it easier for partners and clients to work with some of our advertsing solutions, the gTech team has open sourced this framework as a reference implementation.  Our goal is to make managing data workflows using Google Cloud as fast and re-usable as possible, allowing teams to focus on building advertising solutions.',
  author='Paul Kenjora',
  author_email='kenjora@google.com',
  url='https://github.com/google/bqflow',
  packages=['bqflow', "bqflow.util", "bqflow.task"],
  package_dir = { 
    "bqflow":"",
    "bqflow.util":"bqflow/util",
    "bqflow.task":"bqflow/task",
  },
  include_package_data=False,
  install_requires=REQUIREMENTS,
  entry_points={
    'console_scripts': [
      'bqflow_run = bqflow.run:main',
      'bqflow_auth = bqflow.auth:main',
      'bqflow_cm = bqflow.cm:main',
      'bqflow_dv = bqflow.dv:main',
      'bqflow_bq = bqflow.bq:main',
      'bqflow_schedule_local = bqflow.schedule_local:main',
      'bqflow_schedule_drive = bqflow.schedule_drive:main',
    ]
  },
  license='Apache License, Version 2.0',
  zip_safe=False,
  keywords='bqflow',
  classifiers=[
     'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
  ]
)
