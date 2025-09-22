# --------------------------------------
# Two Pointers Algorithm in Python
# --------------------------------------
# The "two pointers" technique is a common approach used in array and string
# problems. The idea is to use two indices (pointers) that move through the
# data structure from different directions (or at different speeds), in order
# to efficiently solve problems without using nested loops.
#
# Typical use cases:
#   1. Finding pairs in a sorted array that sum to a given target.
#   2. Reversing an array or string in place.
#   3. Removing duplicates from a sorted array.
#   4. Detecting palindromes.
#
# Why it’s efficient:
#   - Instead of using a double loop (O(n^2) time), the two pointers method
#     often reduces complexity to O(n).
#   - It uses constant extra space (O(1)).
#
# Example below:
#   Given a sorted array and a target sum, find all unique pairs of numbers
#   that add up to the target using two pointers.
# --------------------------------------

def two_pointers_sum(arr, target):
    """
    Finds all pairs of numbers in a sorted array that add up to a target value.
    
    Parameters:
        arr (list): A sorted list of integers.
        target (int): The sum we want to find pairs for.
    
    Returns:
        list of tuples: Each tuple contains a pair of numbers that add up to 'target'.
    """
    # Initialize two pointers
    left = 0                     # Start pointer (beginning of the array)
    right = len(arr) - 1         # End pointer (end of the array)
    
    pairs = []  # To store the result pairs

    # Move pointers until they meet
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            # Found a valid pair
            pairs.append((arr[left], arr[right]))
            # Move both pointers inward to search for more pairs
            left += 1
            right -= 1

        elif current_sum < target:
            # If sum is too small, move left pointer to increase it
            left += 1

        else:  # current_sum > target
            # If sum is too large, move right pointer to decrease it
            right -= 1

    return pairs


# --------------------------------------
# Example usage
# --------------------------------------
if __name__ == "__main__":
    # Input must be sorted for this method
    arr = [1, 2, 3, 4, 6, 8, 9, 11]
    target = 10

    result = two_pointers_sum(arr, target)
    print("Array:", arr)
    print("Target:", target)
    print("Pairs that sum to target:", result)
