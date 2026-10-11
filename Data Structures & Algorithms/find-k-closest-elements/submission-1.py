class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        i,j = 0, len(arr)-1
        while i < j:
            mid = (i+j)//2
            if arr[mid] < x:
                i = mid + 1
            else:
                j = mid

        l,r = i-1, i
        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1

            elif r >= len(arr):
                res.append(arr[l])
                l -= 1
            
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return sorted(res)
                