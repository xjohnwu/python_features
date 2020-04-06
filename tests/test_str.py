def test_str_as_char_array():
    string = "Hello"
    splits = [s for s in string]
    assert ['H', 'e', 'l', 'l', 'o'] == splits


def test_split_num():
    num = 31
    splits = [int(s) for s in str(num)]
    assert [3, 1] == splits
