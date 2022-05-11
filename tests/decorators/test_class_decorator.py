from functools import wraps


def decorate_all_functions(function_decorator):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                setattr(cls, name, function_decorator(obj))
        return cls

    return decorator


def print_on_call(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('{} called'.format(func.__name__))
        try:
            res = func(*args, **kw)
        finally:
            print('{} finished'.format(func.__name__))
        return res

    return wrapper


@decorate_all_functions(print_on_call)
class Foo:
    def func1(self):
        print('1')

    def func2(self):
        print('2')


def test_Foo():
    c = Foo()
    c.func1()
    c.func2()
