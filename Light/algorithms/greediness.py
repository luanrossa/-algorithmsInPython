"""
Greedy Algorithm Example in Python
----------------------------------

Problem: Coin Change (minimum coins)

🔎 Idea:
- Always pick the largest coin denomination possible
  until the amount is reduced to zero.

⚡ Key Characteristics of Greedy:
1. Makes locally optimal choices at each step.
2. May or may not lead to the global optimum,
   depending on the problem.

📊 Complexity:
- Time: O(n), where n = number of coin denominations.
- Space: O(1), only storing result.

🎯 Use Cases of Greedy Algorithms:
- Activity selection (interval scheduling).
- Huffman coding (compression).
- Minimum spanning tree (Prim's, Kruskal’s algorithms).
- Coin change (with canonical coin systems).
"""

def greedy_coin_change(coins, amount):
    """
    Greedy coin change algorithm.
    
    :param coins: list of available denominations (must be sorted descending)
    :param amount: total amount to change
    :return: list of chosen coins
    """
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result


# ================== EXAMPLE ==================

coins = [25, 10, 5, 1]   # US coin system
amount = 63

result = greedy_coin_change(coins, amount)
print(f"Coins used to make {amount}: {result}")
print(f"Total coins = {len(result)}")
