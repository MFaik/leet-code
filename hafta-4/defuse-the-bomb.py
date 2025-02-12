# https://leetcode.com/problems/defuse-the-bomb/
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if(n == 1):
            return [0]

        ret = list(range(n))
        if k < 0:
            l, r = n+k, n-1
        else:
            l, r = 1, k
        
        curr_sum = 0
        for i in range(l, r+1):
            curr_sum += code[i]

        for i in range(n):
            ret[i] = curr_sum
            curr_sum -= code[l]
            l = (l+1)%n
            r = (r+1)%n
            curr_sum += code[r]
        return ret
