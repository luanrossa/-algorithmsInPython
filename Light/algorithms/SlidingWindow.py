"""
Sliding Window Algorithm Example
--------------------------------

Problem: Find the maximum sum of any contiguous subarray of size k.

Naive approach:
- Check all possible subarrays of size k (O(n*k)).

Sliding Window approach:
- Use a running sum for the window.
- Slide the window by removing the element going out
  and adding the element coming in (O(n)).

Complexity:
- Time: O(n)
- Space: O(1)
"""

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # Not enough elements

    # Compute initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum


# ================== EXAMPLE ==================

arr = [2, 1, 5, 1, 3, 2]
k = 3

print(f"Maximum sum of a subarray of size {k}:", max_sum_subarray(arr, k))


def longest_unique_substring(s):
    """
    Sliding window for longest substring without repeating characters.
    """
    seen = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1  # shrink window
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# Example
s = "abcabcbb"
print("Longest substring without repeating characters:", longest_unique_substring(s))

"""
Real-World Sliding Window Example
---------------------------------

Problem:
- Given a list of requests per second, find the maximum total
  requests in any 10-second window.

Application:
- Detecting unusual traffic (e.g., DDoS attack detection).
"""

def max_requests_in_window(requests, window_size):
    n = len(requests)
    if n < window_size:
        return None

    # Initial window sum
    window_sum = sum(requests[:window_size])
    max_sum = window_sum

    # Slide the window across the array
    for i in range(window_size, n):
        window_sum += requests[i] - requests[i - window_size]
        max_sum = max(max_sum, window_sum)

    return max_sum


# ================== EXAMPLE ==================

# Requests per second for 20 seconds
requests = [5, 2, 7, 3, 9, 4, 1, 6, 3, 8, 2, 4, 9, 5, 7, 3, 2, 8, 6, 4]

window_size = 10
result = max_requests_in_window(requests, window_size)

print(f"Maximum number of requests in any {window_size}-second window:", result)