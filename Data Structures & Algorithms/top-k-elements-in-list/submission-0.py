class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq_group = [[] for i in range(len(nums)+1)]
        for num in nums:
            counts[num] = 1 + counts.get(num,0)
        for num, freq in counts.items():
            freq_group[freq].append(num)

        res = []
        for i in range(len(freq_group)-1, 0, -1):
            for num in freq_group[i]:
                res.append(num)
                if len(res) == k:
                    return res
        