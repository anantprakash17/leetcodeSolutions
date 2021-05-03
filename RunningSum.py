class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        runningSum = [nums[0]]
        for i in range(1,len(nums)):
            runningSum.append(nums[i] + runningSum[i-1])
        return runningSum
            
