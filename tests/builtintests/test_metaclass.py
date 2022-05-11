def test_new_style_class():
    # https://realpython.com/python-metaclasses/
    class Foo:
        pass

    x = Foo()

    assert Foo == type(x)

    assert type == type(Foo)


def test_builtin_types():
    for t in int, float, dict, list, tuple:
        assert type == type(t)


def test_type():
    """
    type is a metaclass, of which classes are instances.
    Just as an ordinary object is an instance of a class, any new-style class in Python, and thus any class in Python 3,
    is an instance of the type metaclass.
    """
    assert type == type(type)
