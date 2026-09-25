class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        count={}
        for i in s1.split():
            count[i]=count.get(i,0)+1
        for i in s2.split():
            count[i]=count.get(i,0)+1
        result=[]
        for i in count:
            if count[i]==1:
                result.append(i)

        return result              