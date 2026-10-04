class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges==[]:
            return True
        if len(edges)<n-1:
            return False
        graph = {i:set() for i in range(n)}
        for n1,n2 in edges:
            if n1==n2:
                return False
            graph[n1].add(n2)
            graph[n2].add(n1)

        leaf_nodes=set()
        for node in graph:
            if len(graph[node])==1:
                leaf_nodes.add(node)
        print(leaf_nodes, graph)
        for node in leaf_nodes:
            if node in graph:
                graph.pop(node)


        while leaf_nodes:
            for node in graph:
                graph[node]=graph[node].difference(leaf_nodes)
            print(leaf_nodes, graph)
            
            leaf_nodes=set()
            for node in graph:
                # CRITICAL - UNCONNECTED OR 1-CONNECTED NODES ARE LEAVES
                if len(graph[node])<=1:
                    leaf_nodes.add(node)

            for node in leaf_nodes:
                if node in graph:
                    graph.pop(node)
        
        print("Final graph")
        print(graph)
        if graph:
            return False

        return True
        