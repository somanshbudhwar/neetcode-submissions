class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites==[]:
            return [i for i in range(numCourses)]
        graph={i:set() for i in range(numCourses)}
        for course,preq in prerequisites:
            graph[course].add(preq)

        res=[]
        # CRITICAL - KEEP REMOVING LEAF NODES
        leaf_nodes=set([i for i in graph if graph[i]==set()])
        print(leaf_nodes)
        res+=leaf_nodes
        while leaf_nodes:
            for node in leaf_nodes:
                graph.pop(node)
            for course in graph:
                graph[course]=graph[course].difference(leaf_nodes)
            leaf_nodes=set([i for i in graph if graph[i]==set()])
            res+=leaf_nodes
        if graph:
            return []
        return res
            
        

        



        