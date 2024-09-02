#este algoritmo só funciona para n ímpar
import numpy as np

N = 9
magicsquare = np.zeros((N,N),dtype=int)

n= 1
i,j = 0, N//2

while n <= N**2: # n é o numero de casas preenchidas
    magicsquare[i,j] = n
    n+=1
    newi, newj = (i-1) %N, (j+1)%N  #nunca calha nas mesmas coordenadas
    if magicsquare[newi,newj]:
        i +=1 # para evitar passar das margens
    else:
        i, j = newi, newj
print(magicsquare)