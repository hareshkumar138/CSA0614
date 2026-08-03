arr = [13, 41, 19, 36, 8, 50]
comparisons = 0
swaps = 0
n = len(arr)
print("Initial Array:", arr)
for i in range(n - 1):
    print(f"\nPass {i + 1}:")
    for j in range(n - i - 1):
        comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1
        print(arr)
print("\nSorted Array:", arr)
print("Total Comparisons:", comparisons)
print("Total Swaps:", swaps)
