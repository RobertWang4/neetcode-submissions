from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)

        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        order = []
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)

            for i in preMap[node]:
                if not dfs(i):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            order.append(node)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order