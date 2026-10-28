class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestampValues = self.map[key]
        l, r = 0, len(timestampValues) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            if timestampValues[mid][1] <= timestamp:
                result = timestampValues[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return result
