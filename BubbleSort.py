# BubbleSort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # Print the current state of the array
        print(f"Pass {i+1}, Initial array: {arr}")
        # Track swapping
        swapped = False
        for j in range(0, n-i-1):
            # Show comparison
            print(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                # Swapping elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                # Print the array after a swap
                print(f"Swapped {arr[j]} with {arr[j+1]}, Array now: {arr}")
        # If no two elements were swapped, the list is sorted
        if not swapped:
            print("No swaps occurred, array is sorted.")
            break
        # Print the array after each pass
        print(f"After pass {i+1}, Array: {arr}")

# Testing the function with a sample array
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)

"""
Efficiency and Use
Complexity: Bubble sort has a time complexity of O(n²) in the worst and average case scenarios, making it inefficient for large datasets.
Best case: When the list is already sorted, O(n) due to the optimization added.
Use Cases: While not suitable for large datasets, bubble sort’s simplicity makes it a useful teaching tool for understanding sorting algorithms. It may also be practical for small datasets or nearly sorted data.
"""
