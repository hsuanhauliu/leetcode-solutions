class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ Topological Sort with cycle detection
        Time: O(n)
        Space: O(n)
        """
        # build a graph
        graph = self._build_graph(numCourses, prerequisites)
        res = []
        visited = set()
        
        # iterate through all courses
        for num in range(numCourses):
            # perform dfs at each node
            nodes, parents = [], set()
            if not self._dfs(num, graph, nodes, parents, visited):
                return []
            res += nodes
        
        # reverse the list
        return res[::-1]
        
        
    def _build_graph(self, numCourses, prerequisites):
        graph = {num: set() for num in range(numCourses)}
        for course, prev in prerequisites:
            graph[prev].add(course)
        return graph
    
    
    def _dfs(self, node, graph, res, parents, visited):
        # if cycle is detected
        if node in parents:
            return False
        
        # node has been visited
        if node in visited:
            return True
        
        visited.add(node)
        parents.add(node)
        for child in graph[node]:
            if not self._dfs(child, graph, res, parents, visited):
                return False
            
        res.append(node)
        parents.remove(node)
        return True