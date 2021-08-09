matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['a', 'b', 'c']
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]


def printMatrix(matrix):
    width = len(matrix[0])
    height = len(matrix)

    upper = 0
    left = 0
    lower = height - 1
    right = width - 1

    dirSteps = [{'x': 0, 'y': 1},  # left to right
                {'x': 1, 'y': 0},  # upper to lower
                {'x': 0, 'y': -1},  # right to left
                {'x': -1, 'y': 0}]  # lower to upper

    def isOutOfBound(position):
        if (position['x'] < upper or position['y'] < left or
                position['x'] > lower or position['y'] > right):
            return True
        return False

    def updateBounds(dir):
        nonlocal upper
        nonlocal left
        nonlocal lower
        nonlocal right

        if dir == 0:
            upper += 1
        if dir == 1:
            right -= 1
        if dir == 2:
            lower -= 1
        if dir == 3:
            left += 1

    currentPos = {'x': 0, 'y': 0}
    nextPos = {'x': 0, 'y': 0}
    curDir = 0
    curDirStep = dirSteps[curDir]
    for i in range(width * height):
        # do something for currentPos
        print(matrix[currentPos['x']][currentPos['y']])
        nextPos['x'] = currentPos['x'] + curDirStep['x']
        nextPos['y'] = currentPos['y'] + curDirStep['y']
        if isOutOfBound(nextPos):
            updateBounds(curDir)
            curDir = (curDir + 1) % 4
            curDirStep = dirSteps[curDir]
            currentPos['x'] += curDirStep['x']
            currentPos['y'] += curDirStep['y']
        else:
            currentPos['x'] = nextPos['x']
            currentPos['y'] = nextPos['y']


printMatrix(matrix)
print("=" * 5)
printMatrix(matrix2)
