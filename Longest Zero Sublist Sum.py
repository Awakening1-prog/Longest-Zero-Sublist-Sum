class Solution:
    def solve(self, nums):
        res=0
        m=0
        h={}
        for i in range(len(nums)):
            res+=nums[i]
            if res==0:
                m=i+1
            if res not in h:
                h[res]=i
            else:
                m=max(m,i-h[res])
        return m
