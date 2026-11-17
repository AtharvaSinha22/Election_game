from itertools import permutations
import numpy as np

# ILLUSTRATIVE placeholder inputs - replace with your data sheet
players = ["US", "India", "Ethiopia"]
E = {"US": 5.0, "India": 2.9, "Ethiopia": 0.02}   # baseline emissions (Gt)
k = {"US": 1.0, "India": 2.0, "Ethiopia": 4.0}     # abatement cost parameters
B = 7.0                                            # allowed budget (same units)

r = (sum(E.values()) - B) / sum(E.values())        # common cut fraction
R = {i: r * E[i] for i in players}

def c(S):
    if not S: return 0.0
    return (sum(R[i] for i in S))**2 / (2 * sum(1 / k[i] for i in S))

def v(S):
    return sum(c([i]) for i in S) - c(S)

def shapley(players, v):
    phi = {i: 0.0 for i in players}
    perms = list(permutations(players))
    for order in perms:
        S = []
        for i in order:
            phi[i] += v(S + [i]) - v(S)
            S.append(i)
    return {i: phi[i] / len(perms) for i in players}

phi = shapley(players, v)
print(phi, "sum =", sum(phi.values()), "v(N) =", v(players))
