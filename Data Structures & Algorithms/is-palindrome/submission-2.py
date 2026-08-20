class Solution:
    def isPalindrome(self, s: str) -> bool:
        newary = list(s.lower())
        left = 0
        right = len(newary)-1
        


        while left < right:
            while left < right and not newary[left].isalnum():
                left += 1
            while left < right and not newary[right].isalnum():
                right -= 1
            if newary[left] != newary[right]:
                return False
            left += 1
            right -=1

            

        return True
        