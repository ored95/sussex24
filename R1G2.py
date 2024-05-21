'''
Check if every row and column of an n x n matrix contains all numbers
from 1 to n (inclusive)
'''

def Solution(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    
    # check row
    for row in matrix:
        lp = [0] * n
        for e in row:
            if 0 <= e-1 < n:    # common bug
                lp[e-1] = 1
        if sum(lp) != n:
            return False
    
    # check column
    for j in range(n):
        lp = [0] * n
        for i in range(n):
            if 0 <= matrix[i][j]-1 < n:     # common bug
                lp[ matrix[i][j] - 1 ] = 1
        if sum(lp) != n:
            return False
        
    return True

# import test
# test.runTests(Solution)
# Example;
m1 = [[1, 2, 3], [3, 2, 1], [2, 3, 4]]
m2 = [[1, 2, 3], [3, 2, 1], [2, 3, 0]]
m3 = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
m4 = [[1, 2, 3], [3, 2, 1], [2, 3, 2]]
for m in [m1, m2, m3, m4]:
    print(Solution(m))