# -*- coding: utf-8 -*-
'''
Module for Manipulating Data via the Salt DB API
================================================
'''
from __future__ import absolute_import

# Import salt libs
import salt.utils.sdb


__func_alias__ = {
    'set_': 'set',
}


def get(uri):
    '''
    Get a value from a db, using a uri in the form of sdb://<profile>/<key>. If
    the uri provided does not start with sdb://, then it will be returned as-is.

    CLI Example:

    .. code-block:: bash

        salt '*' sdb.get sdb://mymemcached/foo
    '''
    return salt.utils.sdb.sdb_get(uri, __opts__)


def set_(uri, value):
    '''
    Set a value in a db, using a uri in the form of ``sdb://<profile>/<key>``.
    If the uri provided does not start with ``sdb://`` or the value is not
    succesfully set, return ``False``.

    CLI Example:

    .. code-block:: bash

        salt '*' sdb.set sdb://mymemcached/foo bar
    '''
    return salt.utils.sdb.sdb_set(uri, value, __opts__)
