# returns the sorted array arr
def merge_sorted(arr):
    def rev_sort(arr):
        if len(arr) < 2:
            return arr

        m = len(arr)//2
        left = rev_sort(arr[:m])
        right = rev_sort(arr[m:])

        ret = []
        while len(left) > 0:
            if len(right) > 0 and right[-1] < left[-1]:
                ret.append(right[-1])
                right.pop()
            else:
                ret.append(left[-1])
                left.pop()
        while len(right) > 0:
            ret.append(right[-1])
            right.pop()
        ret.reverse()
        return ret

    ret = rev_sort(arr)
    ret.reverse()
    return ret

# sorts the array in place, but still uses O(n) space
def merge_sort_inplace(arr):
    # q is a queue
    # ql points to the first number in queue
    # qr points to the number after the last number
    # [ql, qr) is the range of q
    q = [0]*(len(arr)//2)
    # merges the ranges [l, m) and [m, r) in the array
    def merge(l, m, r):
        ql, qr = 0, 0

        for _ in range(m-l):
            if arr[m] < arr[l] and (not ql < qr or arr[m] < q[ql]):
                q[qr], arr[l] = arr[l], arr[m] 
                qr += 1
                m += 1
            elif ql < qr and q[ql] <= arr[m] and q[ql] <= arr[l]:
                q[qr], arr[l] = arr[l], q[ql]
                ql += 1
                qr += 1
            l += 1
            
        for _ in range(r-l):
            if m < r and (not ql < qr or arr[m] < q[ql]):
                arr[l] = arr[m]
                m += 1
            else:
                arr[l] = q[ql]
                ql += 1
            l += 1
            
    def sort(l, r):
        if l < r-1:
            m = (r-l)//2+l
            sort(l, m)
            sort(m, r)
            merge(l, m, r)
    
    sort(0, len(arr))

if __name__ == "__main__":
    from random import randint

    def is_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    
    for i in range(100000):
        arr_len = randint(1, 10)
        arr = [randint(1, 100000) for _ in range(arr_len)]
        arr_copy = [x for x in arr]

        merge_sort_inplace(arr)
        if not is_sorted(arr):
            h = {}
            for i, n in enumerate(sorted(arr_copy)):
                h[n] = i
            arr_copy = [h[x] for x in arr_copy]
            arr = [h[x] for x in arr]
            print("tried to merge-sort-inplace ", arr_copy)
            print("but got ", arr)
            assert(False)

        if not is_sorted(merge_sorted(arr)):
            h = {}
            for i, n in enumerate(sorted(arr_copy)):
                h[n] = i
            arr_copy = [h[x] for x in arr_copy]
            arr = [h[x] for x in arr]
            print("tried to merge-sort-inplace ", arr_copy)
            print("but got ", arr)
            assert(False)
