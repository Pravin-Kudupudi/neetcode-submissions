class Solution:
   def longestCommonPrefix(self, strs: List[str]) -> str:
      pref = strs[0]
      
      for s in strs:
         i = 0

         while i < len(s) and i < len(pref) and pref[i] == s[i]:
            i += 1
            
         pref = pref[:i]

      return pref


        