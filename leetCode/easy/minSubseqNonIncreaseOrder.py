class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # return subsequence of min no of nums to be greater than sum of numbers not included
        
        # get 2 largest number
        seq = []
        
        nums = sorted(nums)
        
        # if not get the next largest number until greater
        while sum(seq) <= sum(nums):
            maxa = max(nums)
            seq.append(maxa)
            nums.remove(maxa)

            
        return seq
