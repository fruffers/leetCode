class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        counter1 = -1
        biggest = False
        returnList = []
        # traverse kids
        for kid in candies:
            counter1 += 1
            # sum each kid with extracandy in new var
            compar = kid + extraCandies
            counter2 = -1
            # compare to other kids
            for kid2 in candies:
                counter2 += 1
                if counter2 == counter1:
                    pass
                elif compar >= kid2:
                    biggest = True
                else:
                    biggest = False
                    break
            # return true or false for if kid had greatest no. of candies
            returnList.append(biggest)
        return returnList
