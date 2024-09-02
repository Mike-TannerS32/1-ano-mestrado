from ortools.constraint_solver import pywrapcp
import sys

def main(n=4):
    # Create the solver.
    solver = pywrapcp.Solver('Magic square')
    # declare variables
    x = {}
    for i in range(n):
        for j in range(n):
            x[(i, j)] = solver.IntVar(1, n*n, 'x(%i,%i)' % (i, j))
    x_flat = [x[(i,j)] for i in range(n) for j in range(n)]

    # the sum
    s = solver.IntVar(1, n*n*n,'s')
    
    # constraints  
    solver.Add(solver.AllDifferent(x_flat, True))
    [solver.Add(solver.Sum([x[(i,j)] for j in range(n)]) == s) for i in range(n)]
    [solver.Add(solver.Sum([x[(i,j)] for i in range(n)]) == s) for j in range(n)]
    solver.Add(solver.Sum([ x[(i,i)]     for i in range(n)]) == s) # diag 1
    solver.Add(solver.Sum([ x[(i,n-i-1)] for i in range(n)]) == s) # diag 2

    # solution and search
    solution = solver.Assignment()
    solution.Add(x_flat)
    solution.Add(s)
    db = solver.Phase(x_flat,
                      solver.CHOOSE_FIRST_UNBOUND,
                      solver.ASSIGN_CENTER_VALUE
                      )
    solver.NewSearch(db)

    # output
    num_solutions = 0
    while solver.NextSolution():
        print("s:", s.Value())
        for i in range(n):
            for j in range(n):
                print("%2i" % x[(i,j)].Value(), end="")
            print()
        print()
        num_solutions += 1
    solver.EndSearch()

    print()
    print("num_solutions:", num_solutions)
    print("failures:", solver.Failures())
    print("branches:", solver.Branches())
    print("wall_time:", solver.WallTime())

if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)