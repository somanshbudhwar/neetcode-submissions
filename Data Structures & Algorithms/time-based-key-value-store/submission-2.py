class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        def search_recent():
            l=0
            stamps = self.map[key]
            r=len(stamps)-1
            if stamps[l][0]>timestamp:
                return ""
            if stamps[r][0]<timestamp:
                return stamps[r][1]
            
            most_recent = stamps[l][1]
            for stamp in stamps:
                if stamp[0]<=timestamp:
                    most_recent=stamp[1]
                else:
                    return most_recent
            return most_recent


        if key in self.map:
            return search_recent()
        else:
            return ""