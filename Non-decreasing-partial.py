class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        numSort = sorted(nums)
        print(numSort)
        outOfPlace = 0
        i, j = 0, 0
        while i < len(nums) and j < len(numSort):
            print(i, j)
            if nums[i] != numSort[j]:
                outOfPlace += 1
                i += 2
                j += 1
                if outOfPlace >= 2:
                    return False
            else:
                i += 1
                j += 1
        return True

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        seen = []
        for i in range(len(nums)-1):
            seen.append(nums[i])
            if nums[i] > nums[i + 1]:
                remain = nums[i + 1:]
                dupes = [x for x in remain if (x in seen or x == nums[i + 1])]
                print(remain)
                print(dupes)
                if sorted(remain) != remain or len(dupes) > 1:
                    return False
        return True
