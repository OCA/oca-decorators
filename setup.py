#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from setuptools import Command, setup
from setuptools import find_packages
from unittest import TestLoader, TextTestRunner

from os import path

PROJECT = 'oca-decorators'
SHORT_DESC = (
    'This is a library of decorators for Odoo developers.'
)
README_FILE = 'README.rst'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Framework :: Odoo',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 or '
    'later (LGPLv3+)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup_vals = {
    'name': PROJECT,
    'author': 'Odoo Community Association (OCA)',
    'author_email': 'tools@odoo-community.org',
    'description': SHORT_DESC,
    'url': 'https://oca.github.io/%s' % PROJECT,
    'download_url': 'https://github.com/OCA/%s' % PROJECT,
    'license': 'LGPL-3',
    'classifiers': CLASSIFIERS,
}


if path.exists(README_FILE):
    with open(README_FILE) as fh:
        setup_vals['long_description'] = fh.read()


class FailTestException(Exception):
    """ It provides a failing build """
    pass


class Tests(Command):
    """ Run test & coverage, save reports as XML """

    user_options = []  # < For Command API compatibility

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = TextTestRunner(verbosity=1)
        res = t.run(tests)
        if not res.wasSuccessful():
            raise FailTestException()


if __name__ == "__main__":
    setup(
        packages=find_packages(exclude=('tests')),
        use_scm_version=True,
        cmdclass={'test': Tests},
        setup_requires=[
            'setuptools_scm',
        ],
        install_requires=[
            'decorator',
        ],
        **setup_vals
    )
