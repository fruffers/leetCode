#https://leetcode.com/problems/jewels-and-stones/submissions/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        amount = 0
        for let in stones:
            for a in jewels:
                if (let == a):
                    amount += 1
                    break
                    
                    
        return amount
