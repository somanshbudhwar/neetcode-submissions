class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(stamps,target):
            l=0
            r=len(stamps)-1
            most_recent_val = ""

            while l<=r:
                m=(l+r)//2
                if stamps[m][0]==target:
                    return stamps[m][1]
                elif stamps[m][0]<target:
                    most_recent_val=stamps[m][1]
                    l=m+1
                else:
                    r=m-1
            return most_recent_val


        def fetch_recent():
            l=0
            stamps = self.map[key]
            r=len(stamps)-1
            if stamps[l][0]>timestamp:
                return ""
            if stamps[r][0]<timestamp:
                return stamps[r][1]
            
            # Replace this with binary search
            # most_recent = stamps[l][1]
            # for stamp in stamps:
            #     if stamp[0]<=timestamp:
            #         most_recent=stamp[1]
            #     else:
            #         return most_recent
            most_recent = binary_search(stamps,timestamp)
            return most_recent


        if key in self.map:
            return fetch_recent()
        else:
            return ""