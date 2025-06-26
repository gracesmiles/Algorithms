def merge_sort(arr, level=0):
    indent = "  " * level  # Helps visualize the level of recursion
    print(f"{indent}Merge sorting {len(arr)} elements...")
    
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Visualize the current split
        print(f"{indent}Dividing into: {left_half} and {right_half}")

        # Recursive calls with increased level for indentation
        merge_sort(left_half, level+1)
        merge_sort(right_half, level+1)

        i = j = k = 0
        # Merging the divided lists
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            print(f"{indent}Merging: {arr[:k]} (from {left_half} and {right_half})")

        # Handling remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            print(f"{indent}Adding remaining from left: {arr[:k]}")
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            print(f"{indent}Adding remaining from right: {arr[:k]}")

        print(f"{indent}After merge: {arr}")

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)

"""
Time Analysis:
O(logn) 
"""
