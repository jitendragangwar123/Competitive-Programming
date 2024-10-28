# First Method
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_char=defaultdict(int)

        for w in words:
            for c in w:
                count_char[c]+=1
        for c in count_char:
            if count_char[c] % len(words):
                return False
        return True   

# Second Method
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count=Counter()

        for w in words:
            for c in w:
                count[c]+=1
        for c in count.values():
            if c % len(words):
                return False
        return True   
