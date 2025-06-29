# QuickSort

def quick_sort(arr, depth=0):
    print(f"{'  '*depth}Quick sorting: {arr}")
    if len(arr) <= 1:
        return arr  # Base case: An array of zero or one element is sorted.
    else:
        pivot = arr[0]  # Choosing the first element as the pivot for simplicity.
        less_than_pivot = [element for element in arr[1:] if element <= pivot]
        greater_than_pivot = [element for element in arr[1:] if element > pivot]

        print(f"{'  '*(depth+1)}Pivot: {pivot}")
        print(f"{'  '*(depth+1)}Less than pivot: {less_than_pivot}")
        print(f"{'  '*(depth+1)}Greater than pivot: {greater_than_pivot}")

        # Recursively apply quick sort to the partitions and concatenate the results
        sorted_less_than_pivot = quick_sort(less_than_pivot, depth + 1)
        sorted_greater_than_pivot = quick_sort(greater_than_pivot, depth + 1)
        
        result = sorted_less_than_pivot + [pivot] + sorted_greater_than_pivot
        print(f"{'  '*depth}After sorting: {result}")
        return result

# Sample playlist sorting
tracks = [120, 75, 90, 35, 55, 150, 45]
print("Original tracks:", tracks)
sorted_playlist = quick_sort(tracks)
print("Organized tracks:", sorted_playlist)

"""
Efficiency: O(nlogn)
Poor pivort choice --> O(n^2)
"""
