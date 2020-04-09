""" Backspace String Compare
    Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

    Example 1:

    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".
    Example 2:

    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".
    Example 3:

    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".
    Example 4:

    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".
    Ahmed Ibrahim 
    """
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i=len(S)-1
        j=len(T)-1
        while (i >=0 or j >=0 ):
            if(i >=0 and S[i]=='#'):
                count=0
                while(i >=0 and (S[i]=='#' or count!=0)):
                    if S[i] == '#':
                        count+=1
                    else:
                        count-=1
                    i-=1
               
            if(j >=0 and T[j] == '#'):
                count=0
                while(j >= 0 and (T[j]=='#' or count!=0)):
                    if T[j] == '#':
                        count+=1
                    else:
                        count-=1
                    j-=1
                
            if i>=0 and j >=0:
                if(S[i] == T[j]):
                    i-=1
                    j-=1
                else:
                    return False
            elif i < 0 and j < 0:
                continue
            else:
                return False
        return True
