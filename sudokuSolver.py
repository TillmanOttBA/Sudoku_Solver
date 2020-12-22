#Löst das Sudoku, indem eindeutige Lösungen gefunden werden
def solveEasy(sudoku):
    foundSolution = True
    while foundSolution:
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

#Erzeugt ein Array, dass für jedes Zahlenfeld angibt, welche Zahlen möglich sind
def createPosibilityMap(sudoku):
    possibilityMap = [[[]]]
    for row in range(len(sudoku)):
        possibilityMap.append([[]])
        for col in range(len(sudoku[row])):
            possibilityMap[row].append([])
            possibilityMap[row][col].append(0)
            #Berechne, in welchem Block sich das aktuelle Feld befindet
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

#Gibt das Sudoku in der Konsole aus
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



#easy: sudoku = [[6,0,0,4,1,0,3,0,8],[8,0,5,0,6,3,4,0,0],[7,3,0,0,2,0,0,0,1],[0,0,6,1,5,7,0,0,2],[5,7,0,0,0,4,1,0,6],[1,2,0,0,9,6,0,4,0],[3,0,0,0,0,0,0,8,0],[0,6,9,0,3,0,0,5,0],[0,0,7,0,4,0,0,1,0]]
#hard: sudoku = [[0,0,0,0,0,1,0,4,0],[0,3,0,5,0,0,0,2,0],[8,7,1,0,0,0,0,0,0],[0,0,9,0,6,7,2,0,0],[6,0,3,0,9,0,7,0,0],[0,4,7,0,2,0,3,0,0],[9,1,0,0,0,0,0,0,6],[0,6,0,0,0,0,8,0,5],[0,0,0,0,7,4,0,0,0]]
sudoku = inputByRow()
sudoku = solveEasy(sudoku)
printSudoku(sudoku, " ")