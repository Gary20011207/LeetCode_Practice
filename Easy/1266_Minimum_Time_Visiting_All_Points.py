class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            # Move diagonally as much as possible, then move straight
            # This is equivalent to finding the Chebyshev Distance between two points
            total_time += max(abs(x2 - x1), abs(y2 - y1))

        return total_time