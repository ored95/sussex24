'''
Maximum bags with full capacity of rocks
================================================================================================
You have n bags numbers from 0 to n-1. You are given two 0-indexed integer arrays capacity and
rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks.
You are also given an integer additionalRocks, the number of additional rocks you can place in any
of the bags. Return the maximum number of bags that could have full capacity after placing the 
additional rocks in some bags.
'''

def Solution(capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
    n = len(capacity)
    a = sorted([capacity[i] - rocks[i] for i in range(n)])
    
    ans, i, e = 0, 0, True
    while i < n and e:
        additionalRocks -= a[i]
        e = additionalRocks >= 0
        ans += e
        i += 1
    return ans

# import test
# test.runTests(Solution)
# Example;

capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2
print(Solution(capacity, rocks, additionalRocks))