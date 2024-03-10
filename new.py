import random

class Sudoku:

    def __init__(self, game):
        self.game = game
    
    def print(self, filledCoord):

        COLOR_RESET = "\033[0m"
        COLOR_YELLOW = "\033[33m"

        splitter = "-" * 25

        for i in range(len(self.game)):
            if i % 3 == 0 :
                print(splitter)
            str = ""
            for j in range(len(self.game[i])):
                if j % 3 == 0:
                    str += "| "

                val = self.game[i][j]
                if val == None:
                    str += "x "
                else:
                    hasBeenModified = len(list(filter(
                        lambda coord: coord["row"] == i and coord["column"] == j,
                        filledCoord))) == 1

                    if hasBeenModified:
                        str += COLOR_YELLOW

                    str += f"{val}{COLOR_RESET} "

            print(f"{str}|")
        print(f"{splitter}\n")


    def __removeEl(self, list, el):
        if el != None and list.count(el) != 0:
            list.remove(el)

    def __getPossibilities(self, row, column):

        possibilityArr = [i for i in range(1, len(self.game) + 1 )]

        # row possibilities removal
        for el in self.game[row]:
            self.__removeEl(possibilityArr, el)

        # column possibilities removal
        columArr = [self.game[i][column] for i in range(len(self.game))]
        for el in columArr:
            self.__removeEl(possibilityArr, el)

        # chunk possibilities removal
        def getCenter(pos):
            return 3 * (pos // 3) + 1
        
        centerCoord = {
            "row": getCenter(row),
            "column": getCenter(column)
        }

        chunkArr = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                chunkArr.append(self.game[centerCoord["row"] + i][centerCoord["column"] + j])

        for el in chunkArr:
            self.__removeEl(possibilityArr, el)

        return possibilityArr
    
    def run(self):
        while True:
            over = True
            solvable = False
            filledCoord = []

            for row in range(len(self.game)):
                for column in range(len(self.game[row])):

                    if self.game[row][column] != None:
                        continue

                    over = False
                    possibilities = self.__getPossibilities(row, column)

                    if len(possibilities) == 0:
                        return False

                    if len(possibilities) == 1:
                        solvable = True
                        self.game[row][column] = possibilities[0]
                        filledCoord.append({
                            "row": row,
                            "column": column
                        })
           
            if not solvable and len(filledCoord) != 0:
                return False

            if over:
                return True


occ = 1
while True:

    game = []
    for i in range(1, 10):
        row = [None for _ in range(9)]
        for j in range(random.randint(3, 4)):
            row[random.randint(0, 8)] = random.randint(1, 9)
        game.append(row)

    sudoku = Sudoku(game)

    if sudoku.run():
        sudoku.print([])
        break
    else:
        print(f"{occ} test")
        occ += 1