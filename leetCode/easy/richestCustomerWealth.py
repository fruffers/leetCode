# Richest customer wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # did not steal this solution from my friend :P
        return sorted([sum(account) for account in accounts])[-1]
        
