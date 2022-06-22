'''
You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1

'''

'''
this mistake i did here was that i directly jumped into the solution without looking at the constraints
the nums size here is of order of 10, so we must do it in linear time


'''


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        #greedy solution
        if len(nums)==1:
            if k%2!=0: return -1
            else : return nums[0]
        ans=-1
        if 0<=k-2:
            ans=max(ans,max(nums[:k-1]))
        if 0<=k<len(nums):
            ans=max(ans,nums[k])
        return ans
        
        
        
        
        #dynamic programming solution
        @cache
        def top(nums,removed,k):
            # print(nums,removed,k)
            if k==0:
                if nums==[]: return -1
                else: return nums[0]
            if nums==[]:
                return -1
            ans=-1
            for i,v in enumerate(removed):
                ans=max(ans,top([v]+nums,removed[:i]+removed[i+1:],k-1))
            ans=max(ans,top(nums[1:],removed+[nums[0]],k-1))
            return ans
        return top(nums,[],k)