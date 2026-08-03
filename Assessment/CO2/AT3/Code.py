def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
numbers = [64, 25, 12, 22, 11]
print("Original Array:", numbers)
sorted_array = selection_sort(numbers)
print("Sorted Array:", sorted_array)
