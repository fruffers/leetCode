class Solution:
    def reverseWords(self, s: str) -> str:
        a = [i for j in s.split() for i in (j,' ')][:-1]
        store = ""
        for b in range(len(a)):
            store += a[b][::-1]
            
        return store
