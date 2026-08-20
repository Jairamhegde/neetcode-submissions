class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key,value in freq.items():
            bucket[value].append(key)
        topk = []
        for j in range(len(bucket)-1,-1,-1):
            for i in bucket[j]:
                topk.append(i)
                if len(topk)==k:
                    return topk
            

        



