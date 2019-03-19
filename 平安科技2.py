import sys
import bisect
sys.stdin = open("in.txt","r")


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        List = []
        for i in range(k):
            List.append(nums[i])
        List.sort()
        for i in range(k,len(nums)):
            num = nums[i]
            if num > List[-1]:
                List.append(num)
                List.pop(0)
            elif num <= List[0]:
                continue
            else:
                index = bisect.bisect_left(List,num)
                List.insert(index,num)
                List.pop(0)
        return List[-1]






if __name__ == "__main__":

