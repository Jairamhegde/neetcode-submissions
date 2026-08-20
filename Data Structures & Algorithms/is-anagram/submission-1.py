class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable  = [0]* 26
        n1 = len(s)
        n2 = len(t)
        if n1 != n2 :
            return False

        for i in range(n1):
            indx  = ord(s[i]) - 97
            hashtable[indx] += 1
        for j in range(n2):
            indx  = ord(t[j]) - 97
            hashtable[indx] -= 1

        for k in hashtable:
            if k != 0:

                return False
       
        return True


        