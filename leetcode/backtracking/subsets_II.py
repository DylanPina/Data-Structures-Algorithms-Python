class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, subset: List[int]) -> None:
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while (i < len(nums) - 1) and (nums[i] == nums[i + 1]):
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res
