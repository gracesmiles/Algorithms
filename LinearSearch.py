# Linear Search
def linear_search(arr, target):
    print(f"Starting search for {target} in {len(arr)} elements...")
    for i, value in enumerate(arr):
        print(f"Checking element {i}: {value}")
        if value == target:
            print(f"Target '{target}' found at index: {i}")
            return i
    print(f"Target '{target}' not found.")
    return -1

# Sample list and target
arr = [3, 5, 2, 4, 9]
target = 4
linear_search(arr, target)
