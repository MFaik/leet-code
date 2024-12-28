# https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        curr = 1
        for i in target:
            while curr != i:
                curr += 1
                ret.append("Push")
                ret.append("Pop")
            curr += 1
            ret.append("Push")
        return ret
