class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #Loop through the list looking for number that breaks the order
        for i in range(len(nums)-2):
            if nums[i] > nums[i + 1]:
                #It is possible that the order can be fixed by changing the number at 
                # the current position. We need to check the number 2 indicies after to ensure we 
                # can maintain that order. Ex. [4,6,5,5]. Here if we change the list to [4,6,6,5],
                # It still breaks the order, so we need to change the 6 to a 5. That is what this 
                # if statement accounts for.
                if nums[i + 2] < nums [i]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                #Since we can only change one number, which we have, the list must be sorted. 
                # If it is not, then we can assume that it is not possible to keep the list increasing
                # with once change.
                if sorted(nums) != nums:
                    return False
        return True
    
