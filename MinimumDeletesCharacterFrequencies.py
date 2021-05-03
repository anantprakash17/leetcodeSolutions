class Solution:
    def minDeletions(self, s: str) -> int:
        dropped = 0
        countList = list(Counter(s).values())
        countList.sort()
        for i in range(len(countList)-1, 0, -1):
            if countList[i] == countList[i - 1]:
                countList[i] -= 1
                dropped += 1
                dupeList = [x for x in countList if x == countList[i]]
                while len(dupeList) > 1 and 0 not in dupeList:
                    countList[i] -= 1
                    dropped += 1
                    dupeList = [x for x in countList if x == countList[i]]
        return dropped
