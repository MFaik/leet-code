from typing import List

def quicksort(arr: List[int]) -> None:
    def quick_pass(s: int, e: int):
        if e-s <= 1:
            return
        l, r = s+1, e
        pivot = arr[s]
        while True:
            while l < e and arr[l] <= pivot:
                l += 1
            while r > s and arr[r] >= pivot:
                r -= 1
            if l >= r:
                break
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        arr[r], arr[s] = arr[s], arr[r]
        quick_pass(s, r-1)
        quick_pass(r+1,e)
    quick_pass(0, len(arr)-1)

arr = [1, 1, 2, 5, 6, 1, 2, 3, 8, 9, 5, 3, 4, 7, 9, 5, 2, 1, 4, 7, 9, 4, 2, 3, 6, 9, 0, 0, 0]
quicksort(arr)
print(arr)
