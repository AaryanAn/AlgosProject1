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
    num_of_platforms = []
    curr_width_for_platform = 0
    curr_height_for_platform = 0
    curr_paintings_total = 0
    paintings_per_platform = []

    for i in range(n):
        # Create new platform if current platform is FULL
        if widths[i] + curr_width_for_platform > W:
            paintings_per_platform.append(curr_paintings_total)

            num_of_platforms.append(curr_height_for_platform)

            # Reset parameters for next platform

            curr_width_for_platform = 0
            curr_height_for_platform = 0
            curr_paintings_total = 0

        # Append all values to the current shelf (this will be initial since if statement will not be triggered first time)

        curr_paintings_total += 1
        curr_width_for_platform += widths[i]
        curr_height_for_platform += max(curr_height_for_platform, heights[i])
        
        # We must add the last shelf on its own since we rely on the next shelf being finished 
        if curr_paintings_total > 0:
            num_of_platforms.append(curr_height_for_platform)
            paintings_per_platform.append(curr_paintings_total)

        return len(num_of_platforms), sum(num_of_platforms), paintings_per_platform


    # Add you code here
    ############################

    return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    