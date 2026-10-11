from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        
        heapq.heapify(heap)
        q = deque()
        t = 0


        while heap or q:
            t += 1
            if heap:
                f = 1 + heapq.heappop(heap)
                if f :
                    q.append([f,t+n])
            
            if q and q[0][1] == t:
                heapq.heappush(heap,q.popleft()[0])
        return t

