from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        items = self.data[key]
        left, right = 0, len(items) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2

            if items[mid][0] <= timestamp:
                res = items[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res