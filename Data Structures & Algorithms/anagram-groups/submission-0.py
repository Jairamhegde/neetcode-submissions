class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for ana in strs:
            hashtable = [0]*26
            for i in ana:
                idx = ord(i) - 97
                hashtable[idx] += 1
            group[tuple(hashtable)].append(ana)
        return list(group.values())