class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # The idea is to keep track of the longest subsequence present
        # We do this by maintaining an array of counts for the longest subsequence
        lWord1 = len(word1)
        lWord2 = len(word2)

        counts = [[0] * (lWord2 + 1) for _ in range(lWord1 + 1)]
        #print(counts)
        for i in range(1, lWord1 + 1):
            for j in range(1, lWord2 + 1):
                #print(i, j)
                if word1[i - 1] == word2[j - 1]:
                    # We increment the count of the longest subsequence if we find a match
                    counts[i][j] = counts[i - 1][j - 1] + 1
                else:
                    # Here we want to store the count of the previous longest subsequence. 
                    # This can be either from word1 or word2. 
                    if counts[i - 1][j] > counts[i][j - 1]:
                        counts[i][j] = counts[i - 1][j]
                    else:
                        counts[i][j] = counts[i][j - 1]
                #print(counts[i])
        return (lWord1 + lWord2) - 2*counts[i][j]
                
        
