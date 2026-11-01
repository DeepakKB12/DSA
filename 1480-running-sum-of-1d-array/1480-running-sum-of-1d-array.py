class Solution(object):
    def runningSum(self, nums):
        sum = 0
        r = []
        for i in range(len(nums)):
            sum = sum +nums[i]
            r.append(sum)
        
        return r