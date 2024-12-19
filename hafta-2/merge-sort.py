def merge_sort(arr):
    q = [0]*len(arr)
    def merge_sorted(l, m, r):
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
            
    def merge_part(l, r):
        if l < r-1:
            merge_part(l, (r-l)//2+l)
            merge_part((r-l)//2+l, r)
            merge_sorted(l, (r-l)//2+l, r)
    
    merge_part(0, len(arr))

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

        merge_sort(arr)
        if not is_sorted(arr):
            h = {}
            for i, n in enumerate(sorted(arr_copy)):
                h[n] = i
            arr_copy = [h[x] for x in arr_copy]
            arr = [h[x] for x in arr]
            print("tried to sort ", arr_copy)
            print("but got ", arr)
            assert(False)
