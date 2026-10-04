class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if edges==[]:
            return n
        graph={}
        for i in range(n):
            graph[i]=set()
        for n1,n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        
        visited=set()
        all_nodes=set([i for i in graph])

        def dfs(node):
            if node in visited:
                return 
            # CRITICAL - TRAVERSE AND ADD TO VISITED
            visited.add(node)
            new_nodes=graph[node]
            for node in new_nodes:
                dfs(node)
        
        count=0
        while visited!=all_nodes:
            count+=1
            node=next(iter(all_nodes.difference(visited)))
            dfs(node)
        return count
            
        