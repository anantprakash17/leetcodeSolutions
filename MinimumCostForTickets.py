class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costTracker = [0]*(days[-1] + 1)
        
        for i in range(max(days)+1):
            if i not in days:
                costTracker[i] = costTracker[i-1]
            else:
                maxDayPass = costTracker[max(i-30,0)] + costs[2]
                sevenPass = costTracker[max(i-7,0)] + costs[1]
                onePass = costTracker[max(i-1,0)] + costs[0]
                costTracker[i] = min(maxDayPass, sevenPass, onePass)
                
        return costTracker[-1]
