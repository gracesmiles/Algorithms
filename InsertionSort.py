# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Visualize the current state before inserting
        print(f"Inserting {key} into the sorted portion: {arr[:i]}")
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            # Visualize the array after each shift
            print(f"Shifting: {arr[:j+2]}...{arr[j+2:i+1]}, Key: {key}")
        arr[j + 1] = key
        # Visualize the array after insertion
        print(f"Placed {key}: {arr[:i+1]}...{arr[i+1:]}")

# Example array of integers
numerical_arr = [22, 11, 99, 88, 9, 7, 42]
print("Original numerical array:", numerical_arr)
insertion_sort(numerical_arr)
print("Sorted numerical array:", numerical_arr)

# Example array of strings
string_arr = ["banana", "apple", "cherry", "date"]
print("\nOriginal string array:", string_arr)
insertion_sort(string_arr)
print("Sorted string array:", string_arr)

"""
Insertion Sort Steps
1. Start with the second element: 
    - The first element is considered sorted. Begin with the second element as your 'key’. This is the item you’re looking to insert into the sorted part.
2. Compare and shift: 
    - Compare the key with each element in the sorted part (starting from the element immediately to the left of the key). If the key is smaller, shift the sorted element to the right. Continue until you find the correct position for the key.
3. Insert the key: 
    - Once the correct position is found, insert the key. The sorted part of the list now includes one more element.
4. Repeat: 
    - Move to the next element in the list and treat it as the new key. Repeat the process until all elements have been inserted into their correct positions.

Time Complexity: O(n^2)

"""
