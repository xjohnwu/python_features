def test_list_index():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert [1, 2, 3, 4] == l[0:4]
    assert [5, 6, 7, 8] == l[4:8]
    assert [9, 10] == l[8:12]
