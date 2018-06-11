import requests
from MyPickle import *
from io import *

SERVER = 'http://localhost:8888'


def select(what, where, predicate=""):
    # initialize the parameters
    payload = {}
    payload['content'] = what
    payload['table'] = where
    if predicate is not "":
        payload['predicate'] = predicate

    # send http requests
    r = requests.get('{}/select'.format(SERVER), params=payload)
    # retore the tuple object
    return read_from_stream(BytesIO(r.content))


def insert(where, values, which=""):
    payload = {}
    payload['table'] = where
    if which is not "":
        payload['column'] = which
    r = requests.post('{}/insert'.format(SERVER), params = payload,data = values)
    return r.text


def update(where, attributes, values, predicate=""):
    """Update table Set the attributes in the values where predicate is True.

    Cautions:
        No space was allowed beside comma!

    Args:
        attributes: a string of the attributes seperated by ','.
        values: a string of values you wanna assign them into the attributes, also seperated by comma. 

    """
    payload = {}
    payload['table'] = where
    payload['keys'] = attributes
    payload['values'] = values
    if predicate is not "":
        payload['predicate'] = predicate
    r = requests.post('{}/update'.format(SERVER),params = payload)
    return r.text
    


def delete(where, predicate=""):
    payload = {}
    payload['table'] = where
    r = requests.post('{}/delete'.format(SERVER), params = payload,data = predicate)
    return r.text


