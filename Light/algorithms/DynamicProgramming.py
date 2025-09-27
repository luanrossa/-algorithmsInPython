"""
Dynamic Programming Example in Python
-------------------------------------

Problem: Fibonacci Sequence

🔎 Idea:
- Naive recursion recalculates the same subproblems many times 
(exponential time).
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

"""
Dynamic programming is a method for solving complex problems,
but beyond breaking them down, schools often trap students in a cage.
They rely on the naïve recursive minds of young learners,
and teachers, being recursive and naïve themselves,
are not very efficient at guiding them.

Yet one blessed boy will perceive the synchronicity of the Fibonacci sequence
in seemingly random, unconnected places and events.
Through this awareness, he will sense the Akashic Records 
the hidden archive where all knowledge and patterns reside—
and he will understand where the true power lies.
Are the boy able to solve this conundrum?

    What degree should I get where I'm going?
    Why you're goin to college? 
    I'm sorry to be sayin this or bunch of college kids 
    but Im ganna ask you why are you?
    becouse you're smart people you're sitting in a class 
    and you have a professor with a finite mind who studied 
    them as brilliant and knows a lot but he is not a universal 
    repository of knoledge in the subject that he's teaching 
    but sources like Google and so on are I mean the intenet will 
    give you access to everything and we're near in class and 
    the professor is going to explaing this, and you !whoa! excellent 
    would you branch to here please Id like to hear more about that 
    that? -No ist not possible.
    !It's a human finite mind trying to teach teach other finite mind!
    God Almighty in one day if you apply yourself you can learn you
    can could learn more than entire fucking semester in physics of 
    mathematics or anything it breaks my heart to see the sadness 
    of our educational system when at your fingertips is all to 
    acknowledge now you have a brain and got all this is garbage or 
    thats fake or lets see isnt that the beuty of it if question it
    givin a research system that reference someone so let me go and read
    that paper you cant do that that in a fucking college class people, good  
    God Almighty you're wasting your young lives and paying money to do so!
    said that lets get back to reality you all are in class definitely 
    Lobby you administrators to teach cryptocurrency at the least they're 
    gonna waste your time and money please teach you something about. 
        --John McAfee


        Black then white are all I see in my infancy
        Red and yellow then came to be, reaching out to me
        Lets me see
        As below so above and beyond, I imagine
        Drawn beyond the lines of reason
        Push the envelope, watch it bend
        Over thinking, over analyzing separates the body from the mind
        Withering my intuition, missing opportunities and I must
        Feed my will to feel my moment, drawing way outside the lines
        Black then white are all I see in my infancy
        Red and yellow then came to be, reaching out to me
        Lets me see
        There is so much more
        And beckons me to look through to these infinite possibilities
        As below so above and beyond, I imagine
        Drawn outside the lines of reason
        Push the envelope, watch it bend
        Over thinking, over analyzing separates the body from the mind
        Withering my intuition leaving opportunities behind
        Feed my will to feel this moment
        Urging me to cross the line
        Reaching out to embrace the random
        Reaching out to embrace whatever may come
        I embrace my desire to
        I embrace my desire to
        Feel the rhythm, to feel connected
        Enough to step aside and weep like a widow
        To feel inspired
        To fathom the power
        To witness the beauty
        To bathe in the fountain
        To swing on the spiral
        To swing on the spiral to
        Swing on the spiral
        Of our divinity
        And still be a human
        With my feet upon the ground I lose myself
        Between the sounds and open wide to suck it in
        I feel it move across my skin
        I'm reaching up and reaching out
        I'm reaching for the random or whatever will bewilder me
        Whatever will bewilder me
        And following our will and wind we may just go where no one's been
        We'll ride the spiral to the end and may just go where no one's been
        Spiral out, keep going
        Spiral out, keep going
        Spiral out, keep going
        Spiral out, keep going

"""