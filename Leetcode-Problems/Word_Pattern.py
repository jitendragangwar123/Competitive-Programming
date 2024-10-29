class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        s=s.split()

        if len(s)==len(pattern):
            for i in range(len(pattern)):
                if pattern[i] not in d:
                    if s[i] not in d.values():
                        d[pattern[i]]=s[i]
                    else:
                        return False
                else:
                    if pattern[i] in d:
                        if d[pattern[i]]!=s[i]:
                            return False
        else:
            if len(s)>len(pattern) or len(s)<len(pattern):
                return False
        
        return True
        
