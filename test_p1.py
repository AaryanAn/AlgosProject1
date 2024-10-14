from bishoy1 import program1
from bishoy2 import program2


def test_p1_given():
    heights = [21, 19, 17, 16, 11, 5, 1]
    widths = [7, 1, 2, 3, 5, 8, 1]
    assert program1(n=7, W=10, heights=heights,
                    widths=widths) == (3, 42, [3, 2, 2])


def test_p2_given():
    heights = [12, 10, 9, 7, 8, 10, 11]
    widths  = [3, 2, 3, 4, 3, 2, 3]
    assert program2(n=7, W=10, heights=heights,
                    widths=widths) == (3, 30, [3, 1, 3])
