class Solution:
    def minOperations(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            if i%2:
                if s[i]=="0":
                    res+=1
                else:
                    0
            else:
                if s[i]=="1":
                    res+=1
                else:
                    0         

        return min(res,len(s)-res)            
