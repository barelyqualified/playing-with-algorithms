class Solution:
    def generateHashMap(self, s: str) -> dict:
        hashmap = {}
        for x in range(len(s)):    
            if not s[x] in hashmap:
                hashmap[s[x]] = 1
            else:
                hashmap[s[x]] += 1
        
        return hashmap


    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        
        first = self.generateHashMap(s)
        second = self.generateHashMap(t)

        for x in first.keys():
            if x in second:
                print(x)
                if not first[x] == second[x]:
                    return False
            elif x not in second:
                return False
        
        return True
        