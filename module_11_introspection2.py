# -*- coding: utf-8 -*-
from pprint import pprint
import inspect


def introspection_info(name, age):
    return f'Hello! My name is {name}, I am {age} years old.'


res = introspection_info('Maria', 35)
print(res)

info = {'type': type(res).__name__, 'attributes': [], 'methods': []}

for attr in dir(res):
    if callable(getattr(res, attr)):
        info['methods'].append(attr)
    else:
        info['attributes'].append(attr)

    module = inspect.getmodule(res)
    if module is None:
        info['module'] = __name__
    else:
        info['module'] = module.__name__

pprint(info)
