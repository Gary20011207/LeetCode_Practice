import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use negative values to simulate Max-Heap with Python's Min-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            # Pop the two heaviest stones
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            # If they are not equal, push the remainder back
            if y != x:
                heapq.heappush(max_heap, -(y - x))
        # Return the last stone's weight, or 0 if none remain
        return -max_heap[0] if max_heap else 0