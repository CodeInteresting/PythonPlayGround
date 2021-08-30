wordA = list("fish")   # row
wordB = list("childish")  # column


matrix = [[0] * (len(wordB) + 1) for _ in range(len(wordA) + 1)]


def max(a, b):
    return a if a > b else b


print(matrix)
print("---Separate Line---")
for row in range(len(wordA)):
    for col in range(len(wordB)):
        if wordA[row] == wordB[col]:
            matrix[row + 1][col + 1] = matrix[row][col] + 1

for row in matrix:
    print(row)
