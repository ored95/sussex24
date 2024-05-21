'''
Maximum score from removing stones
==============================================================================================
You are playing a solitaire game with three piles of stones of sizes a, b and c respectively.
Each turn you choose two different non-empty piles, take one stone from each, and add 1 point
to your score. The game stops when there are fewer than two non-empty piles (meaning there are
no more available moves)
'''

def Solution(a: int, b: int, c: int) -> int:
    l = sorted([a, b, c])
    res = 0
    while len(l) > 1:
        l[0] -= 1
        l[-1] -= 1
        res += 1
        l = sorted([x for x in l if x > 0])
    return res

# import test
# test.runTests(Solution)
# Example;

a, b, c = 2, 6, 4
print(Solution(a, b, c))