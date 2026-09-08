class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])

        visit = [[False for _ in range(n)] for _ in range(m)]
        chars = []
        for char in word[::-1]:
            chars.append(char)


        start = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == chars[-1]:
                    start.append([i,j])

        def route(i,j):
            if len(chars) == 0:
                ret[0] = True
                return
            for [x,y] in [[0,-1],[0,1],[1,0],[-1,0]]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and not visit[ni][nj] and board[ni][nj] == chars[-1]:
                        eli = chars.pop()
                        visit[ni][nj] = True
                        
                        route(ni, nj)
                        
                        visit[ni][nj] = False
                        chars.append(eli)
                        
                        if ret[0]: 
                            return

        ret = [False]
        for [i, j] in start:
            first_char = chars.pop()
            visit[i][j] = True
            
            if len(chars) == 0:
                return True

            route(i, j)
            visit[i][j] = False
            chars.append(first_char)

            if ret[0]:
                return True

        return ret[0]

        