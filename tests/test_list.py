def test_list_index():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert [1, 2, 3, 4] == l[0:4]
    assert [5, 6, 7, 8] == l[4:8]
    assert [9, 10] == l[8:12]


def test_list_insert():
    li1 = [1, 2, 3]
    li2 = li1.copy()
    assert li2.insert(0, 0) is None
    assert li2 == [0, 1, 2, 3]
