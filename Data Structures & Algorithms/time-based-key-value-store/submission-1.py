class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.table[key]
        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result       
