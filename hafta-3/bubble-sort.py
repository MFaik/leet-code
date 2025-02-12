def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

arr = [2,12,42,1,6,2,1,19,8]
bubble_sort(arr)
print(arr)
