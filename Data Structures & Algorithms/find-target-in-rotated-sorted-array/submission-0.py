class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        index = 0

        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] > nums[j]:
                if target <= nums[mid] and target > nums[j]:
                    j = mid
                else:
                    i = mid + 1
            elif nums[mid] < nums[j]:
                if target > nums[mid] and target <= nums[j]:
                    i = mid + 1
                else: j = mid
            else: 
                index = j
                break
                
        if nums[j] == target:
            return j
        else: return -1