def myfunc(a, b, c=3):
    print(a, b, c)
    return a + b + c


def test_myfunc():
    assert 6 == myfunc(1, 2)

    arg = {"a": 2, "b": 5}
    assert 10 == myfunc(**arg)

    arg = {"a": 1, "b": 2, "c": 3}
    assert 6 == myfunc(**arg)


def test_unexpected_keyword_argument_error():
    try:
        myfunc(a=1, b=2, c=3, d=4)
        assert False
    except TypeError as e:
        print(e)
        assert True


def test_split_args():
    arg = {"b": 10}
    assert 113 == myfunc(a=100, **arg)
    assert 1110 == myfunc(a=100, c=1000, **arg)


def test_multiple_values_for_keyword_argument_error():
    try:
        arg = {"b": 10}
        myfunc(a=100, b=20, **arg)
        assert False
    except TypeError as e:
        print(e)
        assert True


