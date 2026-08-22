class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        # go through board row by row
        # add each num in the col to a set - if duplicates return false
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])


        # go through board col by col
        # add each num in the row to a set - if duplicates return false
        for j in range(cols):
            seen = set()
            for i in range(rows):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        # use hashmap with sets
        # use row and col to hash into specfic set and check if exists
        seen = defaultdict(set)
        for i in range(rows):
            hashRow = i // 3
            for j in range(cols):
                hashCol = j // 3
                if board[i][j] != ".":
                    if board[i][j] in seen[tuple([hashRow, hashCol])]:
                        return False
                    seen[tuple([hashRow, hashCol])].add(board[i][j])

        return True

