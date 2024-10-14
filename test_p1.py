import program1

def test_p1_given():
    heights = [21, 19, 17, 16, 11, 5, 1]
    widths = [7, 1, 2, 3, 5, 8, 1]
    assert program1(n = 7, W = 10, heights = heights, widths = widths) == (3, 42, [3,2,2])