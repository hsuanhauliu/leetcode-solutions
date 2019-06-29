class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        size = len(equations)
        for i in range(size):
            num, deno = equations[i]
            if num not in graph:
                graph[num] = {}
            graph[num][deno] = values[i]
            
            if deno not in graph:
                graph[deno] = {}
            graph[deno][num] = 1 / values[i]
        
        res = []
        for num, deno in queries:
            if num not in graph or deno not in graph:
                res.append(-1.0)
            elif num == deno:
                res.append(1.0)
            else:
                visited = set()
                res.append(self.dfs(num, deno, graph, visited))
        
        return res
    
    
    def dfs(self, root, last, graph, visited):
        visited.add(root)
        for next_node in graph[root]:
            if next_node == last:
                return graph[root][next_node]
            elif next_node not in visited:
                num = self.dfs(next_node, last, graph, visited)
                if num != -1.0:
                    return graph[root][next_node] * num
        return -1.0
