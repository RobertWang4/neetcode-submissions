class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            if a == b:
                continue
            
            heapq.heappush(heap,-1 * abs(a-b))
        
        return -heap[0] if heap else 0