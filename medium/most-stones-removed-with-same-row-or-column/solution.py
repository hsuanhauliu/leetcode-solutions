class Solution(object):
    def removeStones(self, stones):
        """ Union find solution. The number of disjoint sets is the number
        of remaining points.
        """
        graph = {}
        for i, j in stones:
            self.union(i, ~j, graph)
        
        return len(stones) - len({self.find(node, graph) for node in graph})
    
    def union(self, a, b, graph):
        graph.setdefault(a, a)
        graph.setdefault(b, b)
        graph[self.find(a, graph)] = self.find(b, graph)
    
    
    def find(self, x, graph):
        if x != graph[x]:
            graph[x] = self.find(graph[x], graph)
        return graph[x]