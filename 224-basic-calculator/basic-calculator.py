class Solution(object):
    def calculate(self, c):
        """
        :type s: str
        :rtype: int
        """
        result=0
        n=0
        stack=[]
        sign=1
        for ch in c:
            if ch.isdigit():
                n=n*10+int(ch)
            elif ch in "+-":
                result+=sign*n
                n=0
                sign=1 if ch=="+" else -1
            elif ch in "(":
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif ch in ")":
                result+=sign*n
                n=0
                result*=stack.pop()
                result+=stack.pop()
        return result + sign *n   
