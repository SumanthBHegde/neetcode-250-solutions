class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        mid = 0
       
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1 
            else:
                r = mid 
        return l
        
        # if flag ==1:
        #     return mid+1
        # elif flag == 2:
        #     return mid-1

        # if nums[mid]<len(nums):
        #     nums[mid] 