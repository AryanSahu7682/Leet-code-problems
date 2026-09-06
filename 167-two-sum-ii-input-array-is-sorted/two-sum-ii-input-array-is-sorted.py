
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for i in range(len(numbers)):

            # Find the number we need
            complement = target - numbers[i]

            # Check if complement already exists
            if complement in hashmap:
                return [hashmap[complement]+1, i+1]

            # Store number and its index
            hashmap[numbers[i]] = i

        return [-1, -1]
