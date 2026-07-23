from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # go through each row - add to hashset
        # go through each col - add to hashset
        # use int div to add each block into hashset
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            seen = defaultdict(set)
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] in seen[i]:
                        return False
                    seen[i].add(board[i][j])

        for j in range(cols):
            seen = defaultdict(set)
            for i in range(rows):
                if board[i][j] != ".":
                    if board[i][j] in seen[j]:
                        return False
                    seen[j].add(board[i][j])

        seen = defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                seen_row = i // 3
                seen_col = j // 3
                if board[i][j] != ".":
                    if board[i][j] in seen[(seen_row, seen_col)]:
                        return False
                    seen[(seen_row, seen_col)].add(board[i][j])
        
        return True
        

                    