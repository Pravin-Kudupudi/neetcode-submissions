class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        visited = set()

        for i in range(len(strs)):
            if strs[i] in visited:
                continue
            hashMap[strs[i]] = [strs[i]]
            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    visited.add(strs[j])
                    hashMap[strs[i]].append(strs[j])
        return list(hashMap.values())

    
    def isAnagram(self, s: str, t: str) -> bool:
        countS , countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
        