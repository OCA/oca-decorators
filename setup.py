# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from setuptools import Command, setup
from setuptools import find_packages
from unittest import TestLoader, TextTestRunner

from os import environ, path

PROJECT = 'oca-decorators'
SHORT_DESC = (
    'This is a library of decorators for Odoo developers.'
)
README_FILE = 'README.rst'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or '
    'later (LGPLv3+)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

version = environ.get('RELEASE') or environ.get('VERSION') or '0.0.1'

if environ.get('TRAVIS_BUILD_NUMBER'):
    version += 'b%s' % environ.get('TRAVIS_BUILD_NUMBER')


setup_vals = {
    'name': PROJECT,
    'author': 'Odoo Community Association (OCA)',
    'author_email': 'tools@odoo-community.org',
    'description': SHORT_DESC,
    'url': 'https://oca.github.io/%s' % PROJECT,
    'download_url': 'https://github.com/OCA/%s' % PROJECT,
    'license': 'LGPL-3',
    'classifiers': CLASSIFIERS,
    'version': version,
}


if path.exists(README_FILE):
    with open(README_FILE) as fh:
        setup_vals['long_description'] = fh.read()


install_requires = []
if path.exists('requirements.txt'):
    with open('requirements.txt') as fh:
        install_requires = fh.read().splitlines()


class FailTestException(Exception):
    """ It provides a failing build """
    pass


class Tests(Command):
    """ Run test & coverage, save reports as XML """

    user_options = []  # < For Command API compatibility

    def initialize_options(self, ):
        pass

    def finalize_options(self, ):
        pass

    def run(self, ):
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = TextTestRunner(verbosity=1)
        res = t.run(tests)
        if not res.wasSuccessful():
            raise FailTestException()


if __name__ == "__main__":
    setup(
        packages=find_packages(exclude=('tests')),
        cmdclass={'test': Tests},
        tests_require=[
            'mock',
        ],
        install_requires=install_requires,
        **setup_vals
    )
