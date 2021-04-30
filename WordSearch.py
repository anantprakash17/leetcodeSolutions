from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]:
                    if self.recursive_search(board, i, j, word, 1, {(i,j)}):
                        return True
        return False
                    
    
    def recursive_search(self, board, i, j, word, idx, visited):
        if idx == len(word):
            return True

        a, b = len(board), len(board[0])
        if i + 1 < a and (i + 1, j) not in visited and board[i + 1][j] == word[idx]:
            visited.add((i + 1,j))
            if self.recursive_search(board, i + 1, j, word, idx+1, visited):
                return True
        if j + 1 < b and (i, j + 1) not in visited and board[i][j + 1] == word[idx]:
            visited.add((i,j + 1))
            if self.recursive_search(board, i, j + 1, word, idx+1, visited):
                return True
        if i - 1 >= 0 and (i - 1, j) not in visited and board[i - 1][j] == word[idx]:
            visited.add(((i - 1),j))
            if self.recursive_search(board, i - 1, j, word, idx+1, visited):
                return True
        if j - 1 >= 0 and (i, j - 1) not in visited and board[i][j - 1] == word[idx]:
            visited.add((i,j - 1))
            if self.recursive_search(board, i, j - 1, word, idx+1, visited):
                return True
        visited.remove((i,j))
        return False
