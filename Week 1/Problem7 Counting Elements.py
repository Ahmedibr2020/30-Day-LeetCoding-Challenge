""" Counting Elements

    Ahmed Ibrahim 
    """
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mem = {}
        count = 0
        for i in arr:
            mem[i]=1
        for i in arr:
            if(i+1) in mem:
                count+=1
        return count
