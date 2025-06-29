# Recursive Fibonacci Function

def fibonacci(n):
    print(f"Calculating fibonacci({n})")
    if n <= 1:
        print(f"Reached the base case with fibonacci({n}) = {n}")
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print(f"Computed fibonacci({n}) = {result}")
        return result

# Demonstrating the visualization
print("Fibonacci sequence result for position 10:", fibonacci(10))
