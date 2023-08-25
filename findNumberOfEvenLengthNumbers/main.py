class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 if x % 2 == 0 else 0 for x in map(lambda x: len(str(x)), nums))
        
