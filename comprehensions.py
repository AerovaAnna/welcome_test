#!/usr/bin/env python3

"""Перепишите каждую из функций используя вместо циклов списковые включения"""


def square_for(a):
    b = []
    for x in a:
        b.append(x**2)
    return b


def square_compr(a):
    b = [x**2 for x in a]
    pass


def keep_positive_for(a):
    b = []
    for x in a:
        if x > 0:
            b.append(x)
    return b


def keep_positive_compr(a):
    b = [x for x in a if x > 0]
    pass


def make_dict_for(a):
    b = {}
    for x in a:
        b[str(x)] = x
    return b


def make_dict_compr(a):
    # Напишите свой код здесь
    pass


def main():
    a = list(range(-5, 5))
    print(square_for(a))
    print(keep_positive_for(a))
    print(make_dict_for(a))
    assert square_for(a) == square_compr(a)
    assert keep_positive_for(a) == keep_positive_compr(a)
    assert make_dict_for(a) == make_dict_compr(a)


if __name__ == '__main__':
    main()
