from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        j = length - 2
        while j >=0 and not(nums[j] < nums[j+1]):
            j -=1
        if j == -1:
            nums.sort()
            return
        k = length - 1
        while not(nums[k] > nums[j]):
            k-=1
        nums[j] , nums[k] = nums[k],nums[j]
        nums[j+1:]= nums[j+1:][::-1]


if __name__ == "__main__":
    a = [1,2,3]
    A=Solution()
    A.nextPermutation(a)
    print(a)
