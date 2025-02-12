# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one_cnt = 0
        for i in nums:
            if i == 1:
                one_cnt += 1

        n = len(nums)
        l, r = 0, one_cnt-1
        curr_zero_cnt = 0
        for i in range(r+1):
            if nums[i] == 0:
                curr_zero_cnt += 1
        
        ret = curr_zero_cnt
        for i in range(n-1):
            if nums[l] == 0:
                curr_zero_cnt -= 1
            l += 1
            r = (r+1)%n
            if nums[r] == 0:
                curr_zero_cnt += 1
            ret = min(curr_zero_cnt, ret)
        
        return ret
