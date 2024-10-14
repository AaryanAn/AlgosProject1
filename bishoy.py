from turtle import width
from typing import List, Tuple


def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1

    Parameters:
    n (int): number of paintings
    W (int): width of the platform
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    ############################
    paintings = [[heights[0]]]
    width_remaining = W-widths[0]
    for h_i, w_i in zip(heights[1:], widths[1:]):
        if width_remaining-w_i >= 0:
            paintings[-1].append(h_i)
            width_remaining -= w_i
        else:
            width_remaining = W
            paintings.append([h_i])

    total_height = 0

    for shelf in paintings:
        total_height += shelf[0]

    num_paintings = []

    for shelf in paintings:
        num_paintings.append(len(shelf))

    return (len(num_paintings), total_height, num_paintings)


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
