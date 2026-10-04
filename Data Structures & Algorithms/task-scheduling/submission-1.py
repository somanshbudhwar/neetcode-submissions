class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time=0
        q=deque()

        while maxHeap or q:
            time+=1
            # Time skip to Push all the process to front
            if not maxHeap:
                time=q[0][1]
            # If processes are ready to be processed
            else:
                # Complete a process and add it to queue
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            # Now push the cnt of latest process to heap so we get max one
            if q and q[0][1]==time:
                cnt=q.popleft()[0]
                heapq.heappush(maxHeap,cnt)
        return time


        