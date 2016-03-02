"""
Single Dispatch
A form of generic function dispatch where the implementation
is chosen based on the type of a single argument.

Generic Function
A function composed of multiple functions implementing the same operation
for different types.
Which implementation should be used during a call is determined
by the dispatch algorithm.
"""

from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


@fun.register(None)
def nothing(arg, verbose=False):
    print("Nothing.")


fun("Hello, world.")
# Hello, world.
fun("test.", verbose=True)
# Let me just say, test.
fun(42, verbose=True)
# Strength in numbers, eh? 42
fun(['spam', 'spam', 'eggs', 'spam'], verbose=True)
# Enumerate this:
# 0 spam
# 1 spam
# 2 eggs
# 3 spam
fun(None)
# Nothing.

# ---------------------------

import json


@singledispatch
def get_json_value(data):
    raise Exception("This type is not supported")


@get_json_value.register(str)
def _(data):
    data = json.loads(data)
    print(data['my-app'])


@get_json_value.register(dict)
def _(data):
    print(data['my-app'])


my_json_data = '{"my-app": "The best App"}'
my_dict_data = {'my-app': 'The best App'}


get_json_value(my_json_data)
# The best App
get_json_value(my_dict_data)
# The best App
get_json_value(None)
# Exception raised
