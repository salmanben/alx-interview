#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """
    Function to find the minimum number of coins needed to make a total amount
    using the given coin denominations.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp[i] if using this coin reduces the number of coins needed for total i
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means total cannot be met by any number of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
