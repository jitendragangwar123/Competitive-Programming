# First Method
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

# Second Method
class Solution:
    def minOperations(self, s: str) -> int:
        res1 = 0  
        res2 = 0  

        for i, c in enumerate(s):
            if (i % 2 == 0 and c == '1') or (i % 2 == 1 and c == '0'):
                res1 += 1

            if (i % 2 == 0 and c == '0') or (i % 2 == 1 and c == '1'):
                res2 += 1

        return min(res1, res2)
