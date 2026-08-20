class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        removed_char = 0
        def ispalindrome(s,low,high):
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -=1
            return True
        while left < right:
            if s[left] != s[right]:
                 
                res = ispalindrome(s,left+1,right)
                res2 = ispalindrome(s,left,right-1)
                if res or res2:
                    return True
                else:return False
                    
                    
            else:
                left += 1
                right -= 1
        return True
        