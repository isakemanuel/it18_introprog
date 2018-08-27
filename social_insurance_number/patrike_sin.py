def main():
    userInput = input('Enter your personal id: ')
    cleanedStr = cleanStr(userInput)

    if not isValidDate(cleanedStr):
        print('Invalid input')
        return

    if not isValidControlValue(cleanedStr):
        print('Invalid input')
        return

    print('Valid input (Hurra!)')


def cleanStr(idStr):
    cleanedStr = idStr.replace(' ', '')
    cleanedStr = cleanedStr.replace('-', '')
    # Removes hundreds from year
    if len(idStr) == 12:
        idStr = idStr[2:]
    return cleanedStr


daysPerMonthDict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
                6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def isValidDate(idStr):
    strLen = len(idStr)

    if strLen != 10:
        return False

    # Removes year
    idStr = idStr[2:]

    mon = int(idStr[:2])
    idStr = idStr[2:]

    day = int(idStr[:2])

    if mon < 1 or mon > 12 or day < 1 or day > daysPerMonthDict[mon]:
        return False

    return True


def isValidControlValue(idStr):
    factor = 2
    res = ''
    for char in idStr:
        res += str(factor * int(char))
        factor = 1 if factor == 2 else 2

    acc = 0
    for char in res:
        acc += int(char)

    if acc % 10 != 0:
        return False

    return True


main()
