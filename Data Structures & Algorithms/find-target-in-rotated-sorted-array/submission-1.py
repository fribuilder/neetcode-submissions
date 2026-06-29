class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r - l) // 2  + l 

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                if (nums[r] >= target) or (nums[r] < nums[mid]):
                    l = mid + 1
                else:
                    r = mid - 1
            
            if nums[mid] > target:
                if (nums[l] <= target) or (nums[mid] < nums[l]):
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1 if nums[l] != target else l