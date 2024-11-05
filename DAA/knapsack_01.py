def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# User input
n = int(input("Enter the number of items: "))
values = [int(input(f"Enter value for item {i + 1}: ")) for i in range(n)]
weights = [int(input(f"Enter weight for item {i + 1}: ")) for i in range(n)]
capacity = int(input("Enter the knapsack capacity: "))

# Calculate and display the maximum value for the knapsack
max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value in Knapsack = {max_value}")
