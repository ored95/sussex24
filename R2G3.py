'''
Word pattern
'''

def Solution(pattern: str, s: str) -> bool:
    words = s.split()
    if len(words) == len(pattern):
        d = dict()
        for i in range(len(pattern)):
            if pattern[i] not in d.keys():
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
        return True
    return False

# import test
# test.runTests(Solution)
# Example;

pattern, s = "abba", "dog dog dog dog"
print(Solution(pattern, s))