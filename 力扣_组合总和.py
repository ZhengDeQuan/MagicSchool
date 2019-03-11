from typing import List
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur_ans = []
        all_ans = []
        cur_ans_index = []
        all_ans_index =[]
        self.compute(0,candidates,target,cur_ans,all_ans,cur_ans_index,all_ans_index)
        return all_ans


    def compute(self ,start, candidates, target ,cur_ans , all_ans , cur_ans_index , all_ans_index):
        # print("start = ",start)
        if target == 0:
            all_ans.append(cur_ans[:])
            all_ans_index.append(cur_ans_index[:])
            # print("index = ",all_ans_index[-1])
        elif target > 0:
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                ele = candidates[i]
                cur_ans.append(ele)
                cur_ans_index.append(i)
                self.compute(i+1,candidates,target-ele,cur_ans,all_ans , cur_ans_index , all_ans_index)
                cur_ans.pop(-1)
                cur_ans_index.pop(-1)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur_ans = []
        all_ans = []
        self.compute(0,candidates,target,cur_ans,all_ans)
        return all_ans


    def compute(self ,start, candidates, target ,cur_ans , all_ans):
        if target == 0:
            all_ans.append(cur_ans[:])
        elif target > 0:
            for i in range(start,len(candidates)):
                ele = candidates[i]
                cur_ans.append(ele)
                self.compute(i,candidates,target-ele,cur_ans,all_ans)
                cur_ans.pop(-1)

if __name__ == "__main__":
    A= Solution()
    res = A.combinationSum([2,3,5],8)

    for ele in res:
        print(ele)