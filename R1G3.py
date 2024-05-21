'''
Check if one string swap can make strings equal
A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices
'''

def Solution(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n == m:
        idx = []
        for i in range(n):
            if s1[i] != s2[i]:
                idx.append(i)
        if (len(idx) == 0) or \
            (len(idx) == 2 and s1[idx[0]] == s2[idx[1]] and s1[idx[1]] == s2[idx[0]]):
            return True
    return False

# import test
# test.runTests(Solution)
# Example;
s1, s2 = 'bank', 'kanb'
print(Solution(s1, s2))
s2 = 'kand'
print(Solution(s1, s2))