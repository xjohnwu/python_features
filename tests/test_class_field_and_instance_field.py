class Huobi:
    field: float


def test_class_field():

    last_exception = None
    try:
        print(Huobi.field)
        # if a class field only has type declared but not assigned any value
        # then it does not even exist as a class field
    except Exception as e:
        last_exception = e

    assert last_exception is not None

    Huobi.field = 3
    assert Huobi.field == 3

    hb = Huobi()
    assert Huobi.field == 3
    assert hb.field == 3
    hb.field = 10
    assert hb.field == 10

    hb2 = Huobi()
    assert Huobi.field == 3
    assert hb2.field == 3
    hb2.field = 20
    assert hb2.field == 20

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

    del hb.field
    assert hb.field == 5

    Huobi.field = 6
    assert hb.field == 6

    del Huobi.field
    last_exception = None
    try:
        print(Huobi.field)
        # if a class field only has type declared but not assigned any value
        # then it does not even exist as a class field
    except Exception as e:
        last_exception = e

    assert last_exception is not None
