class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp={}
        for i, num in enumerate(numbers):
            print(target, num, mp)
            if num in mp:
                return [mp[num], i+1]
            if target-num not in mp:
                mp[target-num]=i+1
            else:
                return [mp[num],i+1]
        return []