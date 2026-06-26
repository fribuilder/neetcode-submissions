class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key, [])
        if not values:
            return ""
        i, j = 0, len(values) - 1
        while i < j:
            m = j - (j - i) // 2  # upper midpoint
            if values[m][1] <= timestamp:
                i = m              # move right, keeping m
            else:
                j = m - 1
        return values[i][0] if values[i][1] <= timestamp else ""
            
