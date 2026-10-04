class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.backtrack(nums,[],set())
        return self.res

    def backtrack(self, nums, subset, visited):
        if len(visited)==len(nums):
            self.res.append(subset.copy())
            return
        for num in nums:
            if num not in visited:
                subset.append(num)
                visited.add(num)
                self.backtrack(nums,subset,visited)
                subset.pop()
                visited.remove(num)
        