# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current position holds the minimum
        min_idx = i
        print(f"Sorting from position {i}: {arr}")  # Visualizing the current state
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"After selecting '{arr[i]}' at position {i}: {arr}")  # Visualizing post-selection state

# Sample book titles for sorting
books = ["Emma", "David", "Charlie", "Bob", "Alice"]
print("Original list of books:", books)
selection_sort(books)
print("Sorted books:", books)

"""
Complexity: O(n^2)
"""
