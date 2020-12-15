"""
    *args
    Variable Arguments to a function :)

    **kwargs
    Keyword Arguments to a function :)
"""


def fun1(*args):
    print(args)
    # convert tuple to a list
    # my_args = list(args)
    print(type(args))


def fun2(*any_name):
    print(any_name)
    print(type(any_name))


def fun3(**kwargs):
    print(kwargs)
    print(type(kwargs))


def fun4(*args, **kwargs):
    print(args)
    print(type(args))

    print(kwargs)
    print(type(kwargs))


fun1(10, 20, 30)
fun1(10, 20, 30, 40, 50)
fun1(10, 20)

print()

fun2(10, "Hello", "awesome", 2.2)

print()

fun3(a=10, b=20, name="john", age=30, pi=3.14)

print()

fun4(10, 20, 30, a=10, b=20, c=30)