from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True