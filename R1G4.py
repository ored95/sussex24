'''
Number of rectangles that can form the largest square
rectangle[i] = [length_i, width_i]
'''

def Solution(rectangles: list[list[int]]) -> int:
    square = [min(r) for r in rectangles]
    max_square = max(square)
    return square.count(max_square)

# import test
# test.runTests(Solution)
# Example;

rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
print(Solution(rectangles))