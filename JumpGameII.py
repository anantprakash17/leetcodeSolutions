class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        jumps = 0
        
        # Iterate through the list jumping to the optimal indicies until we reach the end.
        while i < len(nums) - 1:
            
            # This checks if we can directly jump from the current index to the end.
            if nums[i] + i + 1 >= len(nums):
                return jumps + 1
            
            # We make a list of all possible indicies we can jump to from the current index.
            possibleJumps = nums[i + 1: i + nums[i] + 1]
            
            # We calculate the biggest jump we can make from the current index, while accounting for
            # moving further as distance from i increases. 
            maxJump = max([(v,(a + i + v + 1)) for a, v in enumerate(possibleJumps)], key=lambda x:x[1])
            
            # The following list is not needed to make the code work but speeds up our code at the cost
            # of taking more space. (faster than 99.3%) it checks if any value exceeds the end of the
            # list. If true, then it would take one jump to that value and one to the end.
            canEnd = [v for a,v in enumerate(possibleJumps) if (a + i + v + 1) >= len(nums) - 1]
            if len(canEnd) > 0:
                return jumps + 2
            
            # It is possible that multiple indicies have the same value, we want the last index that 
            # has the given value, so we make a list and take the index of the last one. 
            maxJumpList = [a for a,v in enumerate(possibleJumps) if v == maxJump[0]]
            maxJumpIndex = maxJumpList[-1]
            i = i + maxJumpIndex + 1
            jumps += 1
        return jumps
