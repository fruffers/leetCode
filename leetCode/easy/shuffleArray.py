#https://leetcode.com/problems/shuffle-the-array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # split array at n into 2 arrays
        x = nums[:n]
        y = nums[n:]
        # return array of pairs
        pairs = zip(x,y)
        arr = [a for x in pairs for a in x]
        
        return arr
