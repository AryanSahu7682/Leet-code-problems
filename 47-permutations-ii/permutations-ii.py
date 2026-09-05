class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        useing = [False] * len(nums)
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if useing[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not useing[i - 1]:
                    continue
                useing[i] = True
                path.append(nums[i])
                backtrack()

                path.pop()
                useing[i] = False

        backtrack()
        return result
        