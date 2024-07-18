class Solution(object):
    def runningSum(self, nums):
        l=[]
        le=len(nums)
        res=0
        for i in range(le):
            res=res+nums[i]
            l.append(res)
        return l


