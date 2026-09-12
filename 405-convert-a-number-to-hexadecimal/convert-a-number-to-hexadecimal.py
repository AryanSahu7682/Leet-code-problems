class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        hexadecimal_character="0123456789abcdef"
        if num<0:
            num+=2**32
        result=""
        while num:

            result=hexadecimal_character[num%16]+result
            num//=16
        return result            
