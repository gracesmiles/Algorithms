def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    return -1  # Target not in list

# Testing the function
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
index = binary_search(arr, target)
if index != -1:
    print(f"Target found at index: {index}")
else:
    print("Target not found.")

"""
Mechanisms:
1. Initialization: Start with two pointers representing the range of the list to be searched: the low (start of the list) and high (end of the list).
2. Find the Middle: Calculate the middle index of the current range (low to high).
3. Comparison:
    - If the middle element matches the target, the search ends successfully.
    - If the middle element is greater than the target, adjust the high pointer one position to the left of the middle element, reducing the search range to the left half.
    - Conversely, if the middle element is less than the target, adjust the low pointer one position to the right of the middle, focusing on the right half.
4. Repeat: Continue the process until the target is found or the search range is exhausted (when low is greater than high).

Time Analysis
O(log n)
"""
