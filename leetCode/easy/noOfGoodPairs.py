#https://leetcode.com/problems/number-of-good-pairs/submissions/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairNo = 0
        # make list of pairs
        # pairs = zip(t[:2], t[1:2])
        # i < j
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (i < j):
                    if (nums[i] == nums[j]):
                        goodPairNo += 1
                    
        return goodPairNo
