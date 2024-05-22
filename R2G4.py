'''
=======================================================
Ques #1. Make Array Zero by Subtracting Equal Amounts
'''

def Solution_Q1(nums: list[int]) -> int:
    s = set(nums)
    s.discard(0)
    return len(s)

# import test
# test.runTests(Solution)
# Example;

nums = [1, 5, 0, 3, 5]
print(Solution_Q1(nums))

'''
=======================================================
Ques #2. Maximum number of words you can type
'''

def Solution_Q2(text: str, brokenLetters: str) -> int:
    if brokenLetters == "":
        return len(text.split())
    return sum([1 for w in text.split() if len(set(w).intersection(set(brokenLetters))) > 0])
    
# import test
# test.runTests(Solution)
# Example;

text = "hello world"
brokenLetters = "d"
print(Solution_Q2(text, brokenLetters))

'''
=======================================================
Ques #3. Sort Even and Odd Indices Independently
'''

def Solution_Q3(nums: list[int]) -> list[int]:
    even, odd = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
    ans = []
    for i in range(len(odd)):
        ans += [even[i], odd[i]]
    if len(even) > len(odd):
        ans += [even[-1]]
    return ans
    
# import test
# test.runTests(Solution)
# Example;

nums = [4, 1, 2, 3]
print(Solution_Q3(nums))

'''
=======================================================
Ques #4. Find Players With Zero or One Losses
'''

def Solution_Q4(matches: list[list[int]]) -> list[list[int]]:
    d = dict()
    for winner, loser in matches:
        if winner not in d.keys():
            d[winner] = 0
        if loser not in d.keys():
            d[loser] = 1
        else:
            d[loser] += 1
    return [sorted([player for player in d if d[player] == 0]),
            sorted([player for player in d if d[player] == 1])]
    
# import test
# test.runTests(Solution)
# Example;

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution_Q4(matches))

'''
=======================================================
Ques #5. Reduce array size to the half
'''

def Solution_Q5_origin(arr: list[int]) -> int:
    """
    Solution without ext. library, just dictionary
    """
    d = dict()
    for x in arr:
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
    dv = sorted([d[x] for x in d], reverse=True)
    s, c, k = len(arr) // 2, 0, 0
    while s > 0:
        s -= dv[k]
        c += 1
        k += 1
    return c

from collections import Counter
def Solution_Q5(arr: list[int]) -> int:
    """
    Solution using Counter()
    """
    cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
    num_freq = sorted(cnt.values(), reverse=True)  # Sort dictionary by their frequency (descending order)
    
    half_size = len(arr) // 2
    ans = 0
    
    while half_size > 0:
        half_size -= num_freq[ans]
        ans += 1
    
    return ans
    
# import test
# test.runTests(Solution)
# Example;

arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(Solution_Q5(arr))
