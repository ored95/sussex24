'''
Destination city, the city without any path outgoing to another city
'''

def Solution(paths: list[list[str]]) -> str:
    d = dict()
    for path in paths:
        if path[0] in d.keys():     # source
            d[path[0]] += 1
        else:
            d[path[0]] = 1

        if path[1] not in d.keys(): # destination
            d[path[1]] = 0
    
    for city in d:
        if d[city] == 0:
            return city
    return ''   # never reached

# import test
# test.runTests(Solution)
# Example;
paths = [
    ['London', 'New York'],
    ['New York', 'Lima'],
    ['Lima', 'Sao Paulo']
]

print(Solution(paths))