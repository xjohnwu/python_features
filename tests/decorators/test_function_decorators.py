def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]

    return inner


@decorator_list
def add_together(a, b):
    return a + b


def test_add_together():
    print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))


# Part 2
def meta_decorator(power):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]

        return inner

    return decorator_list


@meta_decorator(2)
def add_together2(a, b):
    return a + b


def test_add_together2():
    print(add_together2([(1, 3), (3, 17), (5, 5), (6, 7)]))
