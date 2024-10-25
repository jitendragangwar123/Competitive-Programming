class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount=defaultdict(int)
        for c in s:
            charCount[c]+=1
        for (i,c) in enumerate(s):
            if charCount[c]==1:
                return i
        return -1        
