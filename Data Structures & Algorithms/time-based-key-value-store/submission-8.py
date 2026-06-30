from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = self.time_dict[key]
        sort_value = sorted(value, key = lambda x : x[1])
        
        res = None
        l, r = 0, len(sort_value) - 1
        while r >= l:
            mid = (r - l) // 2 + l
            if sort_value[mid][1] <= timestamp:
                res = sort_value[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res if res else ""
            
