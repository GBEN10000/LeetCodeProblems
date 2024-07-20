class Solution(object):
    def majorityElement(self, nums):
        new=list(set(nums))
        dic={}
        count=0
        for i in new:
            for j in nums:
                if i == j:
                    count+=1
                dic[count]=i
            count =0
        return (dic[max(dic)])
