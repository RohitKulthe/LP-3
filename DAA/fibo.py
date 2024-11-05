def fibonacci_recursive(n):
    global recursive_steps
    recursive_steps += 1
    return n if n < 2 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    global iterative_steps
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        iterative_steps += 1
    return a

# Input for Fibonacci number
n = int(input("Enter the value of n: "))

# Recursive approach
recursive_steps = 0
fib_recursive = fibonacci_recursive(n)
print(f"Recursive Fibonacci({n}) = {fib_recursive}")
print(f"Total recursive steps: {recursive_steps}")

# Iterative approach
iterative_steps = 0
fib_iterative = fibonacci_iterative(n)
print(f"Iterative Fibonacci({n}) = {fib_iterative}")
print(f"Total iterative steps: {iterative_steps}")