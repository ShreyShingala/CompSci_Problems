#684. Redundant Connection

from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        print(edges)
        
        def dafult_value():
            return []
        
        graph = defaultdict(dafult_value)
        
        def path_exists(node1, node2):
            if node1 == node2:
                return True
            visited.add(node1)
            print(graph[node1])
            for neighbor in graph[node1]:
                if neighbor not in visited:
                    print(neighbor)
                    print(node2)
                    if path_exists(neighbor, node2):
                        return True
                        
            return False

        for node1, node2 in edges:
            visited = set()
            if path_exists(node1,node2):
                return [node1,node2]
            else:
                graph[node1].append(node2)
                graph[node2].append(node1)

        return None