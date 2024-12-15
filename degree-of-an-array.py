class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        left, right, count = {}, {}, {}
        for i,x in enumerate(nums):
            if not x in count:
                left[x] = i
                count[x] = 0
            right[x] = i
            count[x] += 1
            degree = max(degree, count[x])
        
        ret = len(nums)

        for x in count:
            if count[x] == degree:
                ret = min(right[x] - left[x] + 1, ret)
        
        return ret
'''
this was my original solution, but for some reason takes longer
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        left, right, count = [0]*50000, [0]*50000, [0]*50000
        for i,x in enumerate(nums):
            if count[x] == 0:
                left[x] = i
            right[x] = i
            count[x] += 1
            degree = max(degree, count[x])
        
        ret = len(nums)

        for x in range(50000):
            if count[x] == degree:
                ret = min(right[x] - left[x] + 1, ret)
        
        return ret
'''
