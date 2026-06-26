
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(allowed, perm):
            if not allowed:
                res.append(perm.copy())
                return

            for i in range(len(allowed)):
                # choose allowed[i]
                perm.append(allowed[i])
                new_allowed = allowed[:i] + allowed[i+1:]  # remove it *functionally*
                backtrack(new_allowed, perm)
                perm.pop()

        backtrack(nums, [])
        return res
