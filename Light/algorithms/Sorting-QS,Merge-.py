"""
Sorting Algorithms in Python
----------------------------

Includes:
1. QuickSort
2. MergeSort

Complexities:
- QuickSort: Avg O(n log n), Worst O(n^2)
- MergeSort: O(n log n), guaranteed
"""

# -------------------------
# QuickSort Implementation
# -------------------------
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# -------------------------
# MergeSort Implementation
# -------------------------
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    # Merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ================== EXAMPLE ==================

arr = [38, 27, 43, 3, 9, 82, 10]

print("Original array:", arr)
print("Sorted with QuickSort:", quicksort(arr))
print("Sorted with MergeSort:", mergesort(arr))
