from utils.mathutils import round_to_tick, floor_amount, ceil_amount


def test_round_to_tick():
    assert 0.003 == round_to_tick(0.0031342, 0.001)
    assert 2.788 == round_to_tick(2.78799, 0.001)


def test_ceil_amount():
    assert 0.003 == ceil_amount(0.002813, 3)
    assert 0.0029 == ceil_amount(0.002813, 4)


def test_floor_amount():
    assert 0.002 == floor_amount(0.002813, 3)
    assert 0.0028 == floor_amount(0.002813, 4)
