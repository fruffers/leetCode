class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        output = False
        diff = (max(arr[0],arr[1])) - (min(arr[0],arr[1]))
        for i in range(len(arr)-1):
            if ((max(arr[i],arr[i+1])) - (min(arr[i],arr[i+1]))) == diff:
                pass
            else:
                return False
        return True
