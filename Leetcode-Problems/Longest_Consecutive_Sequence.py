class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums=set(nums)
        longestCS=0
        for num in new_nums:
            if (num-1) not in new_nums:
                length=0
                while (num+length) in new_nums:
                    length+=1
                    longestCS=max(length,longestCS)
        return longestCS            
