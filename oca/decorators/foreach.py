# -*- coding: utf-8 -*-
# Copyright 2004-2015 Odoo S.A.
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from decorator import decorator


def foreach(container=None):
    """ Loop the decorated method and return the results in a new `container`.

    Example:

        .. code-block:: python

            @helpers.foreach(list)
            def method(self):
                return self.id

        If the above method is called on a Record Singleton with the ``id`` 1
        it would return:

            [1]

        If the method is called on a RecordSet containing Records with ``id``
        1, 2, and 3 it would return:

            [1, 2, 3]

        If no container is provided as an argument to the decorator, and a
        value is returned from the decorated method, a ValueError will be
        raised.

        .. code-block:: python

            @helpers.foreach()
            def method(self):
                # Raises ValueError
                return 1+2

            @helpers.foreach()
            def method(self):
                # No error raised
                self.math = 1+2

    Args:
        container (callable): It will be called with an iterable of the
            decorated method results, then returned.

    Raises:
        AssertionError: If no container type is provided, and a value is
            returned from the decorated method. This will only be raised if
            ``PYTHONOPTIMIZE`` is less than 2.
        TypeError: If an incorrect data type is provided as `container`.
            Valid arguments are `None` or any callable.

    Returns:
        mixed: A new `container`, instantiated with the results of the
            decorated method - iterated so that `self` is a singleton.
    """

    def _foreach(method):

        def loop(method, self, *args, **kwargs):
            results = (method(rec, *args, **kwargs) for rec in self)
            if container is None:
                for result in results:
                    assert result is None
            else:
                return container(results)

        wrapper = decorator(loop, method)
        wrapper._helpers = 'foreach'
        return wrapper

    return _foreach
