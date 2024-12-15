class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        step = len(arr)//2
        i = 0
        while step > 0:
            print(i, step)
            right = i+step+1 >= len(arr) or arr[i + step] > arr[i + step+1]
            left = i+step-1 < 0 or arr[i+step] > arr[i+step-1]
            if right and left:
                return i+step
            if left:
                i += step
            step = (step+1) // 2
        return i
