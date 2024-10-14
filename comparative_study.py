import time
import random
import matplotlib.pyplot as plt
from program1 import program1  # Import program1 function from program1.py
from program2 import program2  # Import program2 function from program2.py

def generate_unimodal_input(n: int, W: int):
    """
    Generate random unimodal input with n paintings and platform width W.
    Heights follow a unimodal sequence: first decreasing, then increasing.
    Widths are random integers between 1 and W//2 to ensure the width constraint.
    """
    min_index = random.randint(1, n-2)  # Ensure there's a valid turning point
    decreasing_part = sorted([random.randint(1, 100) for _ in range(min_index)], reverse=True)
    increasing_part = sorted([random.randint(1, 100) for _ in range(n - min_index)], reverse=False)
    heights = decreasing_part + increasing_part
    widths = [random.randint(1, W // 2) for _ in range(n)]
    return heights, widths

def measure_runtime(program_func, n: int, W: int, heights: list[int], widths: list[int]):
    """
    Measure the execution time of a program function (program1 or program2).
    """
    start_time = time.time()
    program_func(n, W, heights, widths)
    end_time = time.time()
    return end_time - start_time

def main():
    n_values = [1000, 2000, 3000, 4000, 5000]  # Different input sizes
    runs_per_n = 5  # Number of datasets per input size
    W = 10  # Platform width
    program1_times = []
    program2_times = []

    # Loop over different input sizes
    for n in n_values:
        print(f"Running experiments for n = {n}...")

        # Initialize variables to accumulate times for multiple runs
        total_time_p1 = 0
        total_time_p2 = 0

        # Run 5 experiments for each n
        for _ in range(runs_per_n):
            # Generate input for Program1 (no need for unimodal pattern)
            heights_p1, widths_p1 = generate_unimodal_input(n, W)

            # Measure runtime for Program1
            time_p1 = measure_runtime(program1, n, W, heights_p1, widths_p1)
            total_time_p1 += time_p1

            # Generate unimodal input for Program2
            heights_p2, widths_p2 = generate_unimodal_input(n, W)

            # Measure runtime for Program2
            time_p2 = measure_runtime(program2, n, W, heights_p2, widths_p2)
            total_time_p2 += time_p2

        # Compute the average time over the 5 runs
        avg_time_p1 = total_time_p1 / runs_per_n
        avg_time_p2 = total_time_p2 / runs_per_n

        # Store the average times
        program1_times.append(avg_time_p1)
        program2_times.append(avg_time_p2)

    # Plotting Program1 runtime
    plt.figure(1)
    plt.plot(n_values, program1_times, label="Program 1 (S1)", color='blue')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Program 1 Runtime vs Input Size')
    plt.legend()
    plt.savefig("program1_runtime.png")  # Save the plot as a PNG file
    plt.show()

    # Plotting Program2 runtime
    plt.figure(2)
    plt.plot(n_values, program2_times, label="Program 2 (S2)", color='green')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Program 2 Runtime vs Input Size')
    plt.legend()
    plt.savefig("program2_runtime.png")  # Save the plot as a PNG file
    plt.show()

if __name__ == "__main__":
    main()
