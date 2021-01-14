# recursive top down
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # dict matrix of length of max square values (r,c) -> squarearea
        
        self.comparea(0,0,ROWS,COLS,cache,matrix)
        return max(cache.values())*max(cache.values())
    
    
    def comparea(self,r,c,ROWS,COLS,cache,matrix):
        if r >= ROWS or c >= COLS:
            return 0
        
        if (r,c) not in cache:
            right = self.comparea(r,c+1,ROWS,COLS,cache,matrix)
            down = self.comparea(r+1,c,ROWS,COLS,cache,matrix)
            diag = self.comparea(r+1,c+1,ROWS,COLS,cache,matrix)
            
            cache[(r,c)] = 0
            
            if matrix[r][c] == "1":
                # get max square val for current cache pos and its possible square area, either 1, or 2
                cache[(r,c)] = 1 + min(right,down,diag)
            
        # return value in cache
        return cache[(r,c)]
