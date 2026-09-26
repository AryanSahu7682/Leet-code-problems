class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tra=[]
        for i in range(numRows):
            row=[1]
            if tra:

                last_row=tra[-1]

                for j in range(len(last_row)-1):
                    row.append(last_row[j]+last_row[j+1])
                row.append(1)
            tra.append(row)
        return tra            
  