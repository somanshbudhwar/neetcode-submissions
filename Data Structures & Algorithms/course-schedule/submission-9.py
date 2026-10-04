class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        indegree=[0]*numCourses
        adj = [[] for _ in range(numCourses)]

        # CRITICAL - INDEGREE OF COURSE IS ZERO AND PREQ INCREASES

        for c,p in prerequisites:
            indegree[p]+=1
            adj[c].append(p)

        q = []
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        finish=0
        while q!=[]:
            node=q.pop(0)
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return finish==numCourses

