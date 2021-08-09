patternRawStr = "abcdabce"
text = "abcdabcffjdabcdabceab"
patternStr = [len(patternRawStr)] + list(patternRawStr)
nextStr = [None] * (patternStr[0] + 1)
nextStr2 = [None] * (patternStr[0] + 1)


def calculateNext(patternStr, nextStr):
    k = 0
    j = 1
    nextStr[1] = 0
    while j < patternStr[0]:
        if (k == 0) or (patternStr[j] == patternStr[k]):
            j += 1
            k += 1
            nextStr[j] = k

        else:
            k = nextStr[k]


def calculateNextImproved(patternStr, nextStr):
    k = 0
    j = 1
    length = patternStr[0]
    nextStr[1] = 0  # nextStr[j] = 0
    while j < length:
        if (k == 0) or (patternStr[j] == patternStr[k]):
            j += 1
            k += 1
            if patternStr[j] == patternStr[k]:
                nextStr[j] = nextStr[k]
            else:
                nextStr[j] = k
        else:
            k = nextStr[k]


# return position of found pattern
def searchText(patternStr, nextStr, text):
    i = 0  # index of text
    j = 1  # index of PatternStr
    foundPos = -1
    lengthText = len(text)
    lengthPatternStr = patternStr[0]
    while i < lengthText and j <= lengthPatternStr:
        if (j == 0) or (patternStr[j] == text[i]):
            i += 1
            j += 1
        else:
            j = nextStr[j]

    if j > lengthPatternStr:
        foundPos = i - lengthPatternStr

    return foundPos


calculateNext(patternStr, nextStr)
calculateNextImproved(patternStr, nextStr2)


print(nextStr)
print(nextStr2)
print(searchText(patternStr, nextStr, text))
print(searchText(patternStr, nextStr2, text))
index = searchText(patternStr, nextStr2, text)

print("Pattern String is %s" % patternRawStr)

for i in range(len(text)):
    if i == index:
        print(" [", end='')
    if i == index + patternStr[0]:
        print("] ", end='')
    print(text[i], end='')
