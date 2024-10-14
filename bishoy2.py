from typing import List, Tuple


def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2

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

    # Add paintings through the first half of the given paintings, same as algorithm 1
    paintings_first = [[heights.pop(0)]]
    
    width_remaining = W-widths.pop(0)
        
    while heights[0] >= heights[1]:
        h_i = heights.pop(0)  
        w_i = widths.pop(0)
        
        if width_remaining - w_i >= 0:
            paintings_first[-1].append(h_i)
            width_remaining -= w_i
        else:
            width_remaining = W - w_i
            paintings_first.append([h_i])     


    paintings_last = [[heights.pop()]]
    width_remaining = W-widths.pop()
    
    while heights:
        h_i = heights.pop()  
        w_i = widths.pop()
        
        if width_remaining - w_i >= 0: 
            paintings_last[-1].append(h_i)
            width_remaining -= w_i
        else:
            width_remaining = W - w_i   
            paintings_last.append([h_i])

    paintings = paintings_first + paintings_last[::-1]
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

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
