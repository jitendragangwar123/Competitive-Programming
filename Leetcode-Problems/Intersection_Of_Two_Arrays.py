class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checked=set(nums1)
        res=[]
        for n in nums2:
            if n in checked and n not in res:
                res.append(n)
        return res 
