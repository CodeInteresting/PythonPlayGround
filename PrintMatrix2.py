matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['a', 'b', 'c']
]


def printMatrix2(matrix):
    width = len(matrix[0])
    height = len(matrix)
    startPos = 0

    def printCircle(startIndex, w, h):
        if w > 0 and h > 0:
            for i in range(startIndex, startIndex + w):
                print(matrix[startIndex][i])
            if h > 1:
                for i in range(startIndex + 1, startIndex + h):
                    print(matrix[i][startIndex + w - 1])
                if w > 1:
                    for i in range(startIndex + w - 2, startIndex - 1, -1):
                        print(matrix[startIndex + h - 1][i])
                    if h > 2:
                        for i in range(startIndex + h - 2, startIndex, -1):
                            print(matrix[i][startIndex])

    while width > 0 and height > 0:
        printCircle(startPos, width, height)
        width -= 2
        height -= 2
        startPos += 1


printMatrix2(matrix)
