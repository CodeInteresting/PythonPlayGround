def PrintNum(str):
    isBeginningZero = True
    for i in range(len(str)):
        if isBeginningZero and (str[i] != 0):
            isBeginningZero = False
        if not isBeginningZero:
            print(str[i], end='')
    if not isBeginningZero:
        print()


def Print1ToN_Digits(n):
    def InnerPrint(aggStr, curIndex):
        if (curIndex == n):
            PrintNum(aggStr)
            return
        for i in range(10):
            aggStr[curIndex] = i
            InnerPrint(aggStr, curIndex + 1)
    digits = [None] * n
    InnerPrint(digits, 0)


Print1ToN_Digits(3)
