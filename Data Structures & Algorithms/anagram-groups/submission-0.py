class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for str in strs:
            s = ''.join(sorted(str))

            if s not in group:
                group[s] = [str] 
            else:
                group[s].append(str)
        
        return list(group.values())