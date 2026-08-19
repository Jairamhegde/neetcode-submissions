class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(nums,k,cap):

            current_cap = 0
            no_of_split = 0

            for i in nums:
                if (i + current_cap) > cap:
                    current_cap = i
                    no_of_split += 1
                else:
                    current_cap += i
            return no_of_split+1


        left,right = max(nums),sum(nums)


        while left <= right:
            mid = (left + right)//2
            res = check(nums,k,mid)
            if res <= k:
                right = mid -1
            else:
                left = mid + 1

        return left
        

        