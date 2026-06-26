class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        output_d = []
        for index, num in enumerate(nums[:n-2]):
            target = -num
            i = index + 1
            j = n - 1
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                else: 
                    output_d.append([-target,nums[i],nums[j]])
                    i += 1
                    j -= 1
        
        seen = set()
        unique = []
        for trip in output_d:
            key = tuple(sorted(trip))  
            if key not in seen:
                seen.add(key)
                unique.append(list(key))

        return unique