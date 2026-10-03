class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in pairs:#closed
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:#open
                stack.append(ch)

        return len(stack) == 0