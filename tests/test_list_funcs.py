from functools import reduce


def test_reduce():
    nums = [1, 2, 3, 3, 2, 1, 4]
    print(reduce(lambda x, y: x ^ y, nums))


def test_map():
    nums = [1, 2, 3, 3, 2, 1, 4]
    print(map(lambda x: x * 2, nums))


def test_filter():
    nums = [1, 2, 3, 3, 2, 1, 4]
    print(filter(lambda x: x > 2, nums))
