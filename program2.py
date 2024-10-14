from typing import List, Tuple
    
def find_minimum_index(heights: List[int]) -> int:
    n = len(heights)
    for i in range(1, n):
        if heights[i] > heights[i - 1]:

            return i - 1  # Found the minimum point where the increase starts
        
    return n - 1  # If no increase is found, the last element is the minimum

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
    ############################
    # Add you code here
    ############################

    # Step 1: Find the minimum point in the unimodal sequence
    
    min_index = find_minimum_index(heights)

    # Step 2: Process from the start to the minimum index

    num_of_platforms = []
    curr_width_for_platform = 0
    curr_height_for_platform = 0
    curr_paintings_total = 0
    paintings_per_platform = []

    # First part (decreasing sequence)
    for i in range(min_index + 1):
        # Create new platform if the current platform is FULL

        if widths[i] + curr_width_for_platform > W:

            paintings_per_platform.append(curr_paintings_total)  # Number of paintings on current platform
            num_of_platforms.append(curr_height_for_platform)  # Max height of current platform

            # Reset parameters for the next platform

            curr_width_for_platform = 0
            curr_height_for_platform = 0
            curr_paintings_total = 0

        # Add painting to the current platform

        curr_paintings_total += 1
        curr_width_for_platform += widths[i]
        curr_height_for_platform = max(curr_height_for_platform, heights[i])
    
    # Add last platform of the first part

    if curr_paintings_total > 0:
        num_of_platforms.append(curr_height_for_platform)
        paintings_per_platform.append(curr_paintings_total)

    # Step 3: Process from the end back to the minimum index

    curr_width_for_platform = 0
    curr_height_for_platform = 0
    curr_paintings_total = 0

    # Second part (increasing sequence)
    for i in range(n - 1, min_index, -1):
        # Create new platform if the current platform is FULL

        if widths[i] + curr_width_for_platform > W:
            paintings_per_platform.append(curr_paintings_total)  # Number of paintings on current platform

            num_of_platforms.append(curr_height_for_platform)  # Max height of current platform


            # Reset parameters for the next platform

            curr_width_for_platform = 0
            curr_height_for_platform = 0
            curr_paintings_total = 0

        # Add painting to the current platform

        curr_paintings_total += 1
        curr_width_for_platform += widths[i]
        curr_height_for_platform = max(curr_height_for_platform, heights[i])

    # Add last platform of the second part

    if curr_paintings_total > 0:
        num_of_platforms.append(curr_height_for_platform)
        paintings_per_platform.append(curr_paintings_total)

    # Step 4: Combine both results (already tracked separately)

    return len(num_of_platforms), sum(num_of_platforms), paintings_per_platform

    #return 0, 0, [] # replace with your code


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    