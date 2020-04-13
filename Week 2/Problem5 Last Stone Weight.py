""" Last Stone Weight

    We have a collection of stones, each stone has a positive integer weight.

    Each turn, we choose the two heaviest stones and smash them together.
    Suppose the stones have weights x and y with x <= y.
    The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed,
    and the stone of weight y has new weight y-x.
    At the end, there is at most 1 stone left.
    Return the weight of this stone (or 0 if there are no stones left.)
    Ahmed Ibrahim 
    """
class Solution(object):
   def lastStoneWeight(self, stones):
      """
      :type stones: List[int]
      :rtype: int
      """
      if len(stones) ==0:
         return 0
      if len(stones) == 1:
         return 1
      while len(stones)>1:
         stones.sort()
         s1,s2=stones[-1],stones[-2]
         if s1==s2:
            stones.pop(-1)
            stones.pop(-1)
         else:
            s1 = abs(s1-s2)
            stones.pop(-1)
            stones[-1] = s1
      if len(stones):
         return stones[-1]
      return 0
