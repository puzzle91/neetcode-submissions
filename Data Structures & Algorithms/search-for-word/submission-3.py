class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        mvs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        def dfs(idx, start):

            if start == len(word):
                return True

            i, j = idx

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False

            if idx in visited:
                return False

            if board[i][j] != word[start]:
                return False

            visited.add(idx)

            for di, dj in mvs:
                if dfs((i + di, j + dj), start + 1):
                    return True

            visited.remove(idx)
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs((i, j), 0):
                    return True

        return False