#Solves the Sudoku by entering all the numbers that can be uniquely determined. May not find a solution for difficult Sudoku puzzles
def solveEasy(sudoku):
    foundSolution = True
    itterationCounter = 0
    while foundSolution:
        print("Starting with itteration " + str(itterationCounter))
        possibilityMap = createPosibilityMap(sudoku)
        foundSolution = False
        for rowBlock in range(3):
            for colBlock in range(3):
                for number in range(1,10):
                    times = 0
                    for checkRow in range(int(rowBlock * 3), int(rowBlock * 3 + 3)):
                        for checkCol in range(int(colBlock * 3), int(colBlock * 3 + 3)):
                            if possibilityMap[checkRow][checkCol][number] == True:
                                times = times + 1
                    if times == 1:
                        for checkRow in range(int(rowBlock * 3), int(rowBlock * 3 + 3)):
                            for checkCol in range(int(colBlock * 3), int(colBlock * 3 + 3)):
                                if possibilityMap[checkRow][checkCol][number] == True:
                                    print("[" + str(checkRow) + ":" + str(checkCol) + "] --> " + str(number))
                                    sudoku[checkRow][checkCol] = number
                                    foundSolution = True
    return sudoku

#Creates an array that indicates for each field which numbers are possible
def createPosibilityMap(sudoku):
    possibilityMap = [[[]]]
    for row in range(len(sudoku)):
        possibilityMap.append([[]])
        for col in range(len(sudoku[row])):
            possibilityMap[row].append([])
            possibilityMap[row][col].append(0)
            #Calculate in wich block the actual field is located
            rowBlock = int((row - row % 3) / 3) 
            colBlock = int((col - col % 3) / 3)
            for number in range(1,10):
                checkFailed = False
                #check occupation
                if sudoku[row][col] != 0:
                    checkFailed = True
                #check row
                for checkCol in range(9):
                    if sudoku[row][checkCol] == number:
                        checkFailed = True
                        break
                #check col
                for checkRow in range(9):
                    if sudoku[checkRow][col] == number:
                        checkFailed = True
                        break
                #check box
                for checkRow in range(int(rowBlock * 3), int(rowBlock * 3 + 3)):
                    for checkCol in range(int(colBlock * 3), int(colBlock * 3 + 3)):
                        if sudoku[checkRow][checkCol] == number:
                            checkFailed = True
                            break
                    if checkFailed:
                        break
                if checkFailed == True:
                    possibilityMap[row][col].append(False)
                else:
                    possibilityMap[row][col].append(True)
    return possibilityMap

#Prints the sudoku in the console
def printSudoku(sudoku, *zeroReplacer):
    if zeroReplacer:
        newRow = []
        rowString = ""
        for row in range(0,9):
            rowString = ""
            for col in range(0,9):
                rowString = rowString + str(sudoku[row][col])
            rowString = rowString.replace("0",str(zeroReplacer[0])[:1])
            newRow = list(rowString)
            if row % 3 == 0:
                print("┼─────────┼─────────┼─────────┼")
            print("│ " + str(newRow[0]) + "  " + str(newRow[1]) + "  " + str(newRow[2]) + " │ " + str(newRow[3]) + "  " + str(newRow[4]) + "  " + str(newRow[5]) + " │ " + str(newRow[6]) + "  " + str(newRow[7]) + "  " + str(newRow[8]) + " │")
        print("┼─────────┼─────────┼─────────┼")
    else:
        actRow = 0
        for row in sudoku:
            if actRow % 3 == 0:
                print("┼─────────┼─────────┼─────────┼")
            print("│ " + str(row[0]) + "  " + str(row[1]) + "  " + str(row[2]) + " │ " + str(row[3]) + "  " + str(row[4]) + "  " + str(row[5]) + " │ " + str(row[6]) + "  " + str(row[7]) + "  " + str(row[8]) + " │")
            actRow = actRow + 1
        print("┼─────────┼─────────┼─────────┼")

#Allows the user to enter the Sudoku row by row
def inputByRow():
    sudoku = [[]]
    for row in range(9):
        sudoku.append([])
        for col in range(9):
            sudoku[row].append(0)

    print("To insert the Sudoku write each Line without any additional spaces. Use any character for empty fields.")
    for row in range(9):
        incorretInput = True
        while incorretInput:
            rowText = input("Insert row " + str(row + 1) + ": ")
            if len(rowText) == 9:
                incorretInput = False
        rowArray = list(rowText)
        for col in range(len(rowArray)):
            if rowArray[col].isnumeric():
                sudoku[row][col] = int(rowArray[col])
            else:
                sudoku[row][col] = 0
        printSudoku(sudoku, " ")
    return sudoku

sudoku = inputByRow()
sudoku = solveEasy(sudoku)
printSudoku(sudoku, " ")