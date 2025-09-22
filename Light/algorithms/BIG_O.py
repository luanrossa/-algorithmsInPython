# --------------------------------------
# Big O Notation in Algorithms
# --------------------------------------
# Big O notation is used to describe the performance (time complexity and space
# complexity) of an algorithm as the input size grows.
#
# Why Big O matters:
#   - It provides a way to evaluate how well an algorithm scales.
#   - Instead of measuring actual execution time (which depends on hardware),
#     Big O focuses on growth rate as input size increases.
#
# Common Big O complexities:
#   - O(1): Constant time → performance does not depend on input size.
#   - O(log n): Logarithmic time → very efficient, input size grows fast
#               but operations grow slowly (e.g., binary search).
#   - O(n): Linear time → work grows directly with input size.
#   - O(n log n): Common for efficient sorting algorithms (merge sort, quicksort).
#   - O(n^2): Quadratic time → nested loops, performance degrades quickly.
#
# Example below:
#   1. Linear Search: O(n)
#      - Scan through all elements until the target is found.
#   2. Binary Search: O(log n)
#      - Requires a sorted list. Repeatedly divide the search interval in half.
# --------------------------------------

def linear_search(arr, target):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    - Worst case: target is at the end or not present at all.
    - Best case: target is the first element.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return the index if found
    return -1  # return -1 if not found


def binary_search(arr, target):
    """
    Binary Search Algorithm (array must be sorted)
    Time Complexity: O(log n)
    - At each step, cut the search space in half.
    - Much faster than linear search for large datasets.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            left = mid + 1  # search in the right half
        else:
            right = mid - 1  # search in the left half
    return -1  # not found


# --------------------------------------
# Example usage
# --------------------------------------
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Search for a number
    target = 15

    print("Array:", arr)
    print("Target:", target)

    # Linear search
    index_linear = linear_search(arr, target)
    print("Linear Search (O(n)) result:", index_linear)

    # Binary search
    index_binary = binary_search(arr, target)
    print("Binary Search (O(log n)) result:", index_binary)
