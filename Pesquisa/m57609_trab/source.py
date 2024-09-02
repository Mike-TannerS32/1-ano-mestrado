from constraint import Problem, AllDifferentConstraint
import timeit

start = timeit.default_timer()
problem = Problem()

men = ['x1', 'x2', 'x3']
women = ['y1', 'y2', 'y3']

men_domain = {
    'x1' : ['y1','y2','y3'],
    'x2' : ['y1', 'y2'],
    'x3' : ['y1', 'y3']
}

for man in men_domain:
    problem.addVariable(man, men_domain[man])

problem.addConstraint(AllDifferentConstraint(), men_domain)

def stable_matching(x1,x2,x3):

    preferences = {
        'x1': [['y1'],['y2','y3']],
        'x2': [['y2'],['y1']],
        'x3': [['y1'],['y3']],
        'y1': [['y1'],['y2','y3']],
        'y2': [['y2'],['y1']],
        'y3': [['y1'],['y3']]
    }

    match = {'x1': x1, 'x2':x2, 'x3':x3}

    def prefers(prefs, p1, p2):
        for group in prefs:
            if p1 in group:
                return True
            if p2 in group:
                return False
        return False

    for man in men:
        woman = match[man]
        for other_woman in women:
            if other_woman != woman and other_woman in men_domain[man]:
                other_man = None
                for m, w in match.items():
                    if w == other_woman:
                        other_man = m
                        break
                if prefers( preferences[man], other_woman, woman) and prefers(preferences[other_woman], man, other_man):
                    return False
    return True

#stability constraint to check matching stability
problem.addConstraint(stable_matching, men)

solutions= problem.getSolutions()

for solution in solutions:
    print(solution)
stop = timeit.default_timer()
print('Time: ', stop - start) 