# https://leetcode.com/problems/find-the-array-concatenation-value/
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ret = 0
        l, r = 0, len(nums)-1
        while l < r:
            ret += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            ret += nums[l]
        return ret
