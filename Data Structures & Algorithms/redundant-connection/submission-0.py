class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        for i in range(1,len(edges)+1):
            graph[i]=set()
        for n1,n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)

        print(graph)
        leaf_nodes=set()
        for node in graph:
            if len(graph[node])<=1:
                leaf_nodes.add(node)
        for node in graph:
            graph[node]=graph[node].difference(leaf_nodes)
        
        while leaf_nodes:
            for node in leaf_nodes:
                graph.pop(node)
            
            leaf_nodes=set()
            for node in graph:
                if len(graph[node])<=1:
                    leaf_nodes.add(node)
            for node in graph:
                graph[node]=graph[node].difference(leaf_nodes)
        
        cycle_edges=[]
        
        for node in graph:
            for n2 in graph[node]:
                cycle_edges.append([node,n2])
        indices=[]
        for e1,e2 in cycle_edges:
            if [e1,e2] in edges:
                indices.append(edges.index([e1,e2]))
            else:
                indices.append(edges.index([e2,e1]))

        return edges[max(indices)]
        