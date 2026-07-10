def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_count(arr[:mid])
    right, inv_right = merge_count(arr[mid:])
    merged = []
    i = j = 0
    inv_count = inv_left + inv_right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count
arr = [2, 4, 1, 3, 5]
sorted_arr, inversions = merge_count(arr)
print("Number of Inversions:", inversions)
