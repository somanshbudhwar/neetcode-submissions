class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, t):
            if arr==[]:
                return False
            l=0
            r=len(arr)-1
            if l==r:
                if arr[0]==t:
                    return True
                else:
                    return False

            mid = int((l+r)/2)
            print(arr,mid,t)
            if arr[mid]==t:
                return True
            if arr[mid]>t:
                return binary_search(arr[l:mid], t)
            else:
                return binary_search(arr[mid+1:r+1], t)
        merged_matrix = []
        for m in matrix:
            merged_matrix+=m
        return binary_search(merged_matrix,target)
