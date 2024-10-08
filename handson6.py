
# Partition function for non-random pivot
def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quicksort function for non-random pivot
def quicksort_non_random(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index
        quicksort_non_random(arr, low, pi - 1)
        quicksort_non_random(arr, pi + 1, high)

        # Example array
arr = [10, 7, 8, 9, 1, 5]

# Call the quicksort function
quicksort_non_random(arr, 0, len(arr) - 1)

# Output the sorted array
print("Sorted array:", arr)

import random

# Reusing the partition function from non-random quicksort
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Partition function with random pivot
def partition_random(arr, low, high):
    rand_pivot = random.randint(low, high)  # Random pivot index
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]  # Swap with the last element
    return partition(arr, low, high)  # Use regular partition logic

# Quicksort function with random pivot
def quicksort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)  # Get pivot index
        quicksort_random(arr, low, pi - 1)  # Recursively sort elements before pivot
        quicksort_random(arr, pi + 1, high)  # Recursively sort elements after pivot

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quicksort_random(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

import sys
import time
import numpy as np
import matplotlib.pyplot as plt

# Increase recursion limit
sys.setrecursionlimit(3000)

# Partition function for non-random pivot
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element is the last element
    i = low - 1  # Index of the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quicksort function for non-random pivot with recursion limit handling
def quicksort_non_random(arr, low, high):
    while low < high:
        # Partition the array
        pi = partition(arr, low, high)

        # Recur only on the smaller partition (optimize tail recursion)
        if pi - low < high - pi:
            quicksort_non_random(arr, low, pi - 1)
            low = pi + 1
        else:
            quicksort_non_random(arr, pi + 1, high)
            high = pi - 1

# Timing function for non-random quicksort
def time_quicksort(arr):
    start_time = time.time()
    quicksort_non_random(arr, 0, len(arr) - 1)
    return time.time() - start_time

# Benchmarking function
def benchmark_quicksort():
    input_sizes = [100, 500, 1000, 5000, 10000, 20000]
    best_times = []
    worst_times = []
    average_times = []

    for size in input_sizes:
        # Best case: already sorted array
        best_case = list(range(size))
        best_times.append(time_quicksort(best_case))

        # Worst case: reverse sorted array
        worst_case = list(range(size, 0, -1))
        worst_times.append(time_quicksort(worst_case))

        # Average case: random array
        average_case = np.random.randint(0, size, size)
        average_times.append(time_quicksort(average_case))

    # Plotting the results
    plt.plot(input_sizes, best_times, label='Best Case', marker='o')
    plt.plot(input_sizes, worst_times, label='Worst Case', marker='o')
    plt.plot(input_sizes, average_times, label='Average Case', marker='o')

    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Benchmark: Best, Worst, and Average Case')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call benchmark function
benchmark_quicksort()
