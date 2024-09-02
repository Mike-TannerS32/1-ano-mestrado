'''Constraint: as letras são diferentes, logo têm numeros diferentes associados entre si'''
'''Constraint: O dobro das concatenação das letras T,W,O é igual à concatenação das letras F,O,U,R '''

for T in range(1, 10):
    for O in range(1, 10):
        for W in range(1,10):
            for F in range(1, 10):
                for U in range(1, 10):
                    for R in range(1, 10):
                        if T == O and T == W and T == R and T == F and T == U and W == R and W == O and W == F and W == U and R == O and R== F and R == U and O == F and O == U and F == U :
                            continue
                        elif 200 * T + 20 * W + 2 * O == 1000 * F + 100 * O + 10 * U + 1 * R:
                            print("Solution: ")
                            print(" ",T, W ,O)
                            print("+", T,W,O)
                            print("----------")
                            print(F,O,U,R, "\n")
                            break
