class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates.sort()

        def backtrack(i: int, target: int) -> None:
            if target == 0:
                res.append(combination[::])
                return
            if (i > len(candidates) - 1) or (target < 0):
                return

            combination.append(candidates[i])
            backtrack(i + 1, target - candidates[i])
        
            while (i < len(candidates) - 1) and (candidates[i] == candidates[i + 1]):
                i += 1
            combination.pop()
            backtrack(i + 1, target)
        
        backtrack(0, target)
        return res