"""
Dynamic Programming Example in Python
-------------------------------------

Problem: Fibonacci Sequence

🔎 Idea:
- Naive recursion recalculates the same subproblems many times (exponential time).
- Dynamic Programming avoids repetition by storing results.

⚡ Two approaches:
1. Memoization (Top-Down) -> recursion with cache.
2. Tabulation (Bottom-Up) -> iterative table filling.

📊 Complexity:
- Time: O(n)
- Space: O(n) for table or recursion stack (can be optimized to O(1)).

🎯 Use Cases of DP:
- Fibonacci numbers
- Knapsack problem
- Longest Common Subsequence
- Matrix chain multiplication
- Shortest paths (e.g., Floyd-Warshall)
"""

# ------------------------
# 1. Top-Down (Memoization)
# ------------------------
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# ------------------------
# 2. Bottom-Up (Tabulation)
# ------------------------
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# ------------------------
# 3. Space Optimized
# ------------------------
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# ================== EXAMPLE ==================

n = 10
print(f"Fibonacci({n}) with Memoization: {fib_memo(n)}")
print(f"Fibonacci({n}) with Tabulation: {fib_tab(n)}")
print(f"Fibonacci({n}) with Space Optimization: {fib_optimized(n)}")

"""
another example: Hash Map Implementation in Python

Dynamic Programming Example: 0/1 Knapsack
-----------------------------------------

Problem:
- Given items with weights and values, and a maximum weight capacity W,
  find the maximum value achievable without exceeding capacity.

Approach:
- Use DP table where dp[i][w] = maximum value achievable
  with first i items and capacity w.

Recurrence:
- If item i is not taken: dp[i][w] = dp[i-1][w]
- If item i is taken:     dp[i][w] = value[i-1] + dp[i-1][w - weight[i-1]]
- Take the max of both choices.

Complexity:
- Time: O(n * W), where n = number of items, W = capacity
- Space: O(n * W) (can be optimized to O(W))

Use Cases:
- Resource allocation
- Budget optimization
- Cargo loading


def knapsack(weights, values, capacity):
    n = len(values)
    # Initialize DP table with zeros
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: include item i-1
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: exclude item i-1
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                # Can't include item i-1
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# ================== EXAMPLE ==================

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = knapsack(weights, values, capacity)
print(f"Maximum value for capacity {capacity} = {result}")
"""