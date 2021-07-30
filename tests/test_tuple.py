def function(pair, oid):
    assert pair == 'HELLO'
    assert oid == 'world'


def test_tuple():
    args = 'HELLO', 'world'
    function(*args)
    args = None, None
    if args[0]:
        assert False


def test_tuple_as_dict_key():
    d = {('Hello', 'world'): 10}
    assert 'Hello', 'world' in d
    assert d['Hello', 'world'] == 10
