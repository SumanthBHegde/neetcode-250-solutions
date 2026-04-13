import itertools

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # temp = list(nums)
        # temp.extend(nums)
        temp = list(itertools.chain(nums,nums))
        return temp