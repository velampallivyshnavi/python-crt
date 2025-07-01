def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: a list of length 0 or 1 is already sorted

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])      # Recursively sort left half
    right_half = merge_sort(arr[mid:])     # Recursively sort right half

    return merge(left_half, right_half)    # Merge the two sorted halves


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Compare elements from left and right lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


# Example usage:
a = [56, 2, 89, 6, 10, 33]
print("Original array:", a)
sorted_a = merge_sort(a)
print("Sorted array:", sorted_a)