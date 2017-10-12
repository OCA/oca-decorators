# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import unittest

from .. import decorators
from .common import TestRecordset


class ForeachRecordset(TestRecordset):

    @decorators.foreach(list)
    def decorated_method_list(self):
        return self

    @decorators.foreach()
    def decorated_method_none(self):
        return

    @decorators.foreach()
    def decorated_method_none_return(self):
        return self


class TestHelpersForeach(unittest.TestCase):

    def setUp(self):
        self.record = ForeachRecordset()
        super(TestHelpersForeach, self).setUp()

    def test_foreach_list(self):
        """ It should iterate and return list of method results. """
        res = self.record.decorated_method_list()
        self.assertEqual(
            res, ForeachRecordset.records,
        )

    def test_foreach_none(self):
        """ It should call the method but return nothing. """
        res = self.record.decorated_method_none()
        self.assertIs(res, None)

    def test_foreach_none_return(self):
        """ It should raise a ValueError if the method returns data. """
        with self.assertRaises(AssertionError):
            self.record.decorated_method_none_return()
