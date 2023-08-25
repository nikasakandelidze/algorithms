class Solution:
    # [-4,-1,0,3,10] 
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        negatives = []
        i = 0
        while i < len(nums):
            current = nums[i]
            squared_current = current**2
            if current < 0:
                negatives.append(squared_current)
            else:
                if len(negatives):
                    next_negative = negatives[-1]
                    if next_negative < squared_current:
                        negatives.pop()
                        result.append(next_negative)
                        i-=1
                    else:
                        result.append(squared_current)
                else:
                    result.append(squared_current)
            i+=1
        for i in range(len(negatives)-1,-1,-1):
            result.append(negatives[i])
        return result
                
            
        
