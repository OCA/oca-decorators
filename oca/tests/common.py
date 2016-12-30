# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


class TestRecordset(object):
    """ It provides a mock RecordSet for testing """

    records = ['test1', 'test2']
    iter_count = 0

    def __iter__(self):
        for record in self.records:
            yield record
            self.iter_count += 1
