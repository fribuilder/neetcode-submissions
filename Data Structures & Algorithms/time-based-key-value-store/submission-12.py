from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.time_map:
            self.time_map[key] = [(value,timestamp)]
        elif key in self.time_map:
            self.time_map[key].append((value,timestamp))
        else: 
            self.time_map[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        #sorted_pairs = self.time_map[key]
        #sorted_pairs.sort(key = lambda x : x[1])
        if key not in self.time_map:
            return ''

        pairs = self.time_map[key]
        l, r = 0, len(pairs) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if pairs[mid][1] <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return '' if res == -1 else pairs[res][0]
            
