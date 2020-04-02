from utils.mathutils import round_to_tick


def test_round_to_tick():
    assert 0.003 == round_to_tick(0.0031342, 0.001)
    assert 2.788 == round_to_tick(2.78799, 0.001)
