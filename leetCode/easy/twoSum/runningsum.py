# Running Sum of 1D array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # add all nums in array in running order
        adder = 0
        newLine = []
        for num in nums:
            adder += num
            newLine.append(adder)
            
        return newLine
