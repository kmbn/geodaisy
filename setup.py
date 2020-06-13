#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'geodaisy'
DESCRIPTION = 'Python GeoJSON, WKT, and __geo_interface__ made easy.'
URL = 'https://github.com/kmbn/geodaisy'
EMAIL = 'kmbn@nevermindtheumlauts.com'
AUTHOR = 'Kevin Brochet-Nguyen'
REQUIRES_PYTHON = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*'
VERSION = '0.1.1'
REQUIRED = []  # Required packages

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Make sure 'README.md' is present in th MANIFEST.in!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = [('test', None,
                     'Perform a test upload to test.pypi.org if set.')]

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        """Set default values for options."""
        # Each user option must be listed here with their default value.
        self.test = False

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        if self.test:
            repository = '--repository-url https://test.pypi.org/legacy/ '
        else:
            repository = ''

        self.status('Building Source distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(
            sys.executable))

        files = os.listdir('dist/')
        source_dist = [f for f in files if f.endswith('tar.gz')][0]
        wheel_dist = [f for f in files if f.endswith('whl')][0]

        self.status('Uploading Source distribution to PyPi via Twine…')
        os.system('twine upload {0}dist/{1}'.format(repository, source_dist))

        self.status('Uploading Wheel distribution to PyPi via Twine…')
        os.system('twine upload {0}dist/{1}'.format(repository, wheel_dist))

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=REQUIRED,
    setup_requires=['setuptools>=38.6.0'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
