from typing import List

def Perm(array, begin , end):
    if begin >= end:
        print(array)
    for i in range(begin , end):
        array[begin], array[i] = array[i] , array[begin]
        Perm(array,begin+1,end)
        array[begin], array[i] = array[i] , array[begin]

def PermWithRepeat(array , begin , end):
    if begin >= end:
        print(array)
    for i in range(begin,end):
        # if i != begin and array[i] == array[begin]:
        #     continue
        if array[i] in array[begin:i]:#从begin 到 i - 1的数据都与 begin 交换过,如果第 i 的数据与前面begin 到i - 1中的数据有重复，那么不用交换了
            continue
        array[i] , array[begin] = array[begin] , array[i]
        PermWithRepeat(array,begin+1,end)
        array[i] , array[begin] = array[begin] , array[i]

def PermNonRecursive(array):
    array.sort()
    print(array)
    length = len(array)
    while True:
        j = length - 2
        while j >= 0 and not (array[j] < array[j+1]):
            j -=1
        if j == -1:
            break
        k = length - 1
        while  not ( array[k] > array[j]):
            k-=1
        array[k], array[j] = array[j] , array[k]
        array[j+1:] = array[j+1:][::-1]
        print(array)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.P(nums,0,len(nums))
        return self.ans

    def P(self,nums , begin , end):
        if begin >= end:
            self.ans.append(nums[:])
        for i in range(begin , end):
            nums[i] , nums[begin] = nums[begin] , nums[i]
            self.P(nums,begin+1,end)
            nums[i] , nums[begin] = nums[begin] , nums[i]


class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.P(nums,0 , len(nums))
        return self.ans


    def P(self, nums ,begin , end):
        if begin >= end:
            self.ans.append(nums[:])

        for i in range(begin , end):
            if nums[i] in nums[begin:i]:
                continue
            nums[i] , nums[begin] = nums[begin] , nums[i]
            self.P(nums,begin+1, end)
            nums[i] , nums[begin] = nums[begin] , nums[i]


class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        length = len(nums)
        nums.sort()
        self.ans.append(nums[:])
        while True:
            j = length - 2
            while j>=0 and not( nums[j] < nums[j+1]):
                j-=1
            if j == -1:
                break
            k = length - 1
            while not (nums[k] > nums[j]):
                k -= 1
            nums[j] , nums[k] = nums[k] , nums[j]
            nums[j+1:] = nums[j+1:][::-1]
            self.ans.append(nums[:])
        return self.ans


if __name__ == "__main__":
    # Perm([1,2,3],0,len([1,2,3]))
    # PermWithRepeat([1,1,2],0,3)
    # PermNonRecursive([1,2,1])
    A = Solution3()
    res = A.permuteUnique([2,2,1,1])
    print(res)