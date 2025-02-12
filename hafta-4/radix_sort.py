import math

def radix_sort(arr, k):
    assert(k > 1)
    assert(hasattr(arr, "__len__"))
    def radix_sort_step(arr, mod):
        if mod == 0 or len(arr) <= 1:
            return arr
        ret = []
        boxes = {}
        for i in arr:
            boxes.setdefault((i%(mod*k))//mod, []).append(i)
        for i in range(k):
            ret.extend(radix_sort_step(boxes.get(i, []), mod//k))
        return ret
    
    if len(arr) == 0:
        return []
    
    largest = max(arr)
    n = int(math.log(largest, k))
    return radix_sort_step(arr, k**n)

print(radix_sort([1,3,423,4213,8,5,3,234,2412], 10))
