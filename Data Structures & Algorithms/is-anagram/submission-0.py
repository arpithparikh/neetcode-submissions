class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] not in hashmap or hashmap[t[i]] == 0:
                return False
            hashmap[t[i]] -= 1
            
        return True