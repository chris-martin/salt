# -*- coding: utf-8 -*-
'''
A runner module to collect and display the inline documentation from the
various module types
'''
# Import Python libs
import itertools

# Import salt libs
import salt.client
import salt.runner
import salt.wheel


def __virtual__():
    '''
    Always load
    '''
    return True


def runner():
    '''
    Return all inline documentation for runner modules

    CLI Example:

    .. code-block:: bash

        salt-run doc.runner
    '''
    client = salt.runner.RunnerClient(__opts__)
    ret = client.get_docs()
    return ret


def wheel():
    '''
    Return all inline documentation for wheel modules

    CLI Example:

    .. code-block:: bash

        salt-run doc.wheel
    '''
    client = salt.wheel.Wheel(__opts__)
    ret = client.get_docs()
    return ret


def execution():
    '''
    Collect all the sys.doc output from each minion and return the aggregate

    CLI Example:

    .. code-block:: bash

        salt-run doc.execution
    '''
    client = salt.client.get_local_client(__opts__['conf_file'])

    docs = {}
    for ret in client.cmd_iter('*', 'sys.doc', timeout=__opts__['timeout']):
        for v in ret.itervalues():
            docs.update(v)

    i = itertools.chain.from_iterable([i.items() for i in docs.itervalues()])
    ret = dict(list(i))

    return ret


# Still need to modify some of the backend for auth checks to make this work
def __list_functions(user=None):
    '''
    List all of the functions, optionally pass in a user to evaluate
    permissions on
    '''
    client = salt.client.get_local_client(__opts__['conf_file'])
    funcs = {}
    gener = client.cmd_iter(
            '*',
            'sys.list_functions',
            timeout=__opts__['timeout'])
    for ret in gener:
        funcs.update(ret)
    if not user:
        progress(funcs)
        return funcs
    for _, val in __opts__['external_auth'].items():
        if user in val:
            pass
