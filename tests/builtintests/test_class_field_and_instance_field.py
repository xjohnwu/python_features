import pytest


class Huobi:
    field: float


def test_class_field():
    with pytest.raises(AttributeError, match="type object 'Huobi' has no attribute 'field'"):
        # if a class field only has type declared but not assigned any value
        # then it does not even exist as a class field
        print(Huobi.field)

    Huobi.field = 3
    assert Huobi.field == 3

    hb = Huobi()
    assert hb.field == 3
    hb.field = 10
    assert hb.field == 10
    assert Huobi.field == 3

    hb2 = Huobi()
    assert hb2.field == 3
    hb2.field = 20
    assert hb2.field == 20
    assert Huobi.field == 3

    Huobi.field = 4
    print(Huobi.field)
    assert Huobi.field == 4

    hb3 = Huobi()
    assert hb3.field == 4
    hb3.field = 40
    assert hb3.field == 40
    Huobi.field = 5
    assert hb3.field == 40
    assert hb.field == 10
    assert hb2.field == 20
    assert hb3.field == 40

    del hb.field  # This erases instance field, restore class field
    assert hb.field == 5
    Huobi.field = 6  # Set class field will show up in instance field
    assert hb.field == 6

    del Huobi.field
    with pytest.raises(AttributeError, match="type object 'Huobi' has no attribute 'field'"):
        # if a class field only has type declared but not assigned any value
        # then it does not even exist as a class field
        print(Huobi.field)
