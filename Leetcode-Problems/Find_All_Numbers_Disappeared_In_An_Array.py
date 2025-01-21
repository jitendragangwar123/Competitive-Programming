class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums=set(nums)
        temp=[]
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                temp.append(i)
        return temp
