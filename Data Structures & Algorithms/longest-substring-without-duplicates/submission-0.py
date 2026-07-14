class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_length = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1

            while freq[s[i]] > 1:
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, i-left +1)
        return max_length
            

        