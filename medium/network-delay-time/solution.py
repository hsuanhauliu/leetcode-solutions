class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = self._build_graph(times, n)
        return self._find_minimum_time(graph, k, n)
    
    
    def _build_graph(self, times, n):
        graph = {node: {} for node in range(1, n + 1)}
        for start, end, time in times:
            graph[start][end] = time
        return graph
    
    def _find_minimum_time(self, graph, start, n):
        visited = set()
        curr_time = [0] * n
        visited.add(start)
        
        while len(visited) < n:
            # for each node in visited
            source, target, minimum, found = 0, 0, float('inf'), False
            for source_node in visited:
                # find all edges going from node to unvisited nodes
                for end_node, cost in graph[source_node].items():
                    if end_node not in visited and cost + curr_time[source_node-1] < minimum:
                        source, target, minimum, found = source_node, end_node, cost + curr_time[source_node-1], True
                        
            if found:
                visited.add(target)
                curr_time[target-1] = minimum
            else:
                return -1
        
        return max(curr_time)