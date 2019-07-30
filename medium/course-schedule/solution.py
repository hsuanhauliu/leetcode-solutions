class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
	""" Detect cycle. If a cycle exists then it's not able to finish.
	Time: O(n)
	Space: O(n)
	"""
        graph = self._build_graph(numCourses, prerequisites)
        visited = set()
        for node in range(numCourses):
            checked = set()
            if self.found_cycle(node, graph, checked, visited):
                return False
        return True
        
    def _build_graph(self, num_nodes, edges):
        graph = {num: set() for num in range(num_nodes)}
        for b, a in edges:
            graph[a].add(b)
        return graph
    
    def found_cycle(self, root, graph, checked, visited):
        """ DFS """
        if root in checked:
            return True
        
        if root in visited:
            return False
        
        visited.add(root)
        checked.add(root)
        for child in graph[root]:
            if self.found_cycle(child, graph, checked, visited):
                return True
        checked.remove(root)
        return False