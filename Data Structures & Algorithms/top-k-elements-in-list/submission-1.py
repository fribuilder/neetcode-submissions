class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        counts = dict(sorted(counts.items(), reverse = True, key = lambda x:x[1]))
        return list(counts.keys())[:k]
        