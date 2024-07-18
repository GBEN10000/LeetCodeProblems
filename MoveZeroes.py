class Solution(object):
    def moveZeroes(self, nums):
        li=[]
        li2=[]
        for i in nums:
            if i != 0:
                li.append(i)
            else:
                li2.append(i)
        
        nums[:]=li+li2
        
