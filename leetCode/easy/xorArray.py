#https://leetcode.com/problems/xor-operation-in-an-array/submissions/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*a for a in range(0,n)]
        end = nums[0]
        for i in range(1,len(nums)):
            end ^= nums[i]
            
        return end
