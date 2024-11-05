def fractional_knapsack(values, weights, capacity):
    items = sorted([(v / w, v, w) for v, w in zip(values, weights)], reverse=True)
    total_value = 0
    for ratio, v, w in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += ratio * capacity
            break
    return total_value

# User input
n = int(input("Enter number of items: "))
values = [float(input(f"Value of item {i+1}: ")) for i in range(n)]
weights = [float(input(f"Weight of item {i+1}: ")) for i in range(n)]
capacity = float(input("Enter knapsack capacity: "))

# Calculate and display result
print(f"Maximum value in Knapsack = {fractional_knapsack(values, weights, capacity)}")
