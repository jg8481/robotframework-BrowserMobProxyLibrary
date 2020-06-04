#!/usr/bin/env python

import sys
from os.path import join, dirname
from setuptools import setup


CURDIR = dirname(__file__)
with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

sys.path.append(join(CURDIR, 'src'))

filename = join(CURDIR, 'src', 'BrowserMobProxyLibrary', 'version.py')
if sys.version_info.major >= 3:
    exec(compile(open(filename).read(), filename, 'exec'))
else:
    execfile(filename)

with open(join(CURDIR, 'README.md')) as f:
    DESCRIPTION = f.read()

setup(name         = 'robotframework-browsermobproxylibrary',
      version      = VERSION,
      description  = 'BrowserMob Proxy library for Robot Framework',
      long_description = DESCRIPTION,
      long_description_content_type='text/markdown',
      author       = 'Marcin Mierzejewski',
      author_email = '<mmierz@gmail.com>',
      url          = 'https://github.com/s4int/robotframework-BrowserMobProxyLibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing selenium selenium2 webdriver web browsermob proxy',
      platforms    = 'any',
      classifiers  = [
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Testing",
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      install_requires = REQUIREMENTS,
      package_dir = {'': 'src'},
      packages    = ['BrowserMobProxyLibrary'],
      )
