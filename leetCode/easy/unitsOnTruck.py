class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # get max num of units from boxes onto truck
        
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        res = 0
        boxes = 0
        
        for box in boxTypes:
            if boxes == truckSize:
                break
            if boxes + box[0] <= truckSize:
                res+=box[0]*box[1]
                boxes+=box[0]
                continue
            else:
                while (boxes + box[0] > truckSize):
                    box[0] = box[0]-1
            res += box[1]*box[0]
            boxes += box[0]
        return res
