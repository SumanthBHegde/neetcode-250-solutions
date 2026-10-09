class TimeMap:

    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value,timestamp))
        else: 
            self.data[key] = [(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            item = self.data[key]
            for x,y in reversed(item):
                if y <= timestamp:
                    return x
        
        return ""
