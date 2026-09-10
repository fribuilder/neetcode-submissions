from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        position = [[]  for _ in range(len(nums) + 1)]
        res = []
        for key, value in count.items():
            position[value].append(key)
        for i in range(len(nums), -1, -1):
            for num in position[i]:
                res.append(num)
                if len(res) == k:
                    return res

        