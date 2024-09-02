'''Constraints: a rainha não deve ocupar a mesma casa que outra rainha
                a rainha não deve ocupar uma casa que esteja na mesma coluna, linha e diagonal que outra rainha'''





#print(board)

#def solve(self, n:int) -> List[List[str]]:
n = 4
col = set() # coluna
posDiag = set() # (r+c) diagonal negativa
negDiag = set() # (r-c) diagonal negativa

res = [] # resultado
board = [["."]*n for i in range(n)] #tabuleiro inicial

def backtracking(r):
    if r==n: #caso base (fim de linha)
        copy = ["".join(row) for row in board]
        res.append(copy)
        return
    for c in range(n):
        if c in col or (r+c) in posDiag or (r-c) in negDiag: # se estiver presente na coluna, ou na diagonal positiva ou na diagonal negativa
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = "Q"
        
        backtracking(r+1)
        
        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = "."
backtracking(0)
print(res)


