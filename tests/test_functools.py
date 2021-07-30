from functools import cached_property


class CachedPropertyCls:
    def __init__(self):
        self._count = 0

    def get_data(self):
        self._count += 1
        return f"data{self._count}"

    @cached_property
    def p(self):
        return self.get_data()


def test_cached_p():
    c = CachedPropertyCls()
    for i in range(1000):
        assert 'data1' == c.p
    del c.p
    assert 'data2' == c.p
    del c.p
    assert 'data3' == c.p
