class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        def backtrack(a,open , close):
            if len(a)==2*n:
                result.append(a)
                return 
            if open <n:
                backtrack(a+"(",open+1,close)
            if close < open:
                backtrack(a+")",open,close+1)
        backtrack("",0,0)
        return result        