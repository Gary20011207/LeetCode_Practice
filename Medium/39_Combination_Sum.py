class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        # Sorting allows us to stop early (Pruning)
        candidates.sort()
        # Depth First Search for Backtracking
        def backtrack(remain, path, start):
            # Base case
            if remain == 0:
                results.append(path.copy())
                return
            # Explore potential candidates starting from 'start' index
            for i in range(start, len(candidates)):
                # Pruning
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                # Recursion (Stay at current index 'i' to allow reusing the same number)
                backtrack(remain - candidates[i], path, i)
                # Backtrack (Undo the choice)
                path.pop()

        backtrack(target, [], 0)

        return results