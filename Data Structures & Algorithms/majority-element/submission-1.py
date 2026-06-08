class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        maj_element = -1
        for num in nums:
            if cnt == 0:
                maj_element = num
                cnt = 1
            else:
                if maj_element == num:
                    cnt += 1
                else:
                    cnt -= 1
        return maj_element
        
        