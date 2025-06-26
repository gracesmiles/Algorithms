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

"""
Best-case scenario O(1): The target is the first list element.
Worst-case scenario O(n): The target is the last element or not present.
Average case O(n): Assuming uniform distribution, the search examines half the list, simplifying to O(n)
"""
