class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = list(nums)
        temp.extend(nums)
        return temp