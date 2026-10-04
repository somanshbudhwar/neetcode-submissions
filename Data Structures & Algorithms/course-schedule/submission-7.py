class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            preMap[course].append(preq)

        visiting=set()

        def dfs(course):
            if course in visiting:
                return False
            if preMap[course]==[]:
                return True
            
            visiting.add(course)

            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            
            visiting.remove(course)
            preMap[course]=[]
            return True

            
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        
        return True