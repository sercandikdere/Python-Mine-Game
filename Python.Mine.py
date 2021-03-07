import random

class Mine:
    def __init__(self):
        self.letter="M"
        self.random_places=[random.randint(1,7) for i in range(8)]
        self.matrix=[[["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],    # S : this is you
                      ["S","_","_","_","_","_","_","_"],    # starting point
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"]]]

    def settleMines(self):
        for i in range(1):
            for j in range(7):
                if j == 0:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                elif j == 1:
                    self.matrix[i][j][self.random_places[j]]= self.letter
                    self.matrix[i][j+1][self.random_places[j+1]] = self.letter
                elif j == 2:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                elif j == 3:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                    self.matrix[i][j][self.random_places[j + 3]] = self.letter
                elif j == 4:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                elif j == 5:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                elif j == 6:
                    self.matrix[i][j][self.random_places[j]] = self.letter
                elif j == 7:
                    self.matrix[i][j][self.random_places[j]] = self.letter
        return self.matrix

    def matrixx(self):
        matrix=[[["_", "_", "_", "_", "_", "_", "_", "_"],
          ["_", "_", "_", "_", "_", "_", "_", "_"],
          ["_", "_", "_", "_", "_", "_", "_", "_"],
          ["S", "_", "_", "_", "_", "_", "_", "_"],
          ["_", "_", "_", "_", "_", "_", "_", "_"],
          ["_", "_", "_", "_", "_", "_", "_", "_"],
          ["_", "_", "_", "_", "_", "_", "_", "_"]]]
        return matrix

    def showArea(self,row,col):
        self.matrix2=[[["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["S","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"],
                      ["_","_","_","_","_","_","_","_"]]]

        self.matrix2[0][row][col]="S"
        for i in self.matrix2:
            for j in i:
                print(j)

    def findMine(self,row,col,matrix):
        if "M" in matrix[0][row][col]:
            print("You hit the mine")
            ask = input("Do you want continue (Y/N) :")
            if ask == "Y":
                self.advance()
            elif ask == "N":
                quit()
        else:
            pass

    def findS(self,matrix):
        for i in matrix:
            for j in i:
                if "S" in j[7]:
                    print("Congratulations!!! You have reached the end")
                    quit()
                else:
                    pass

    def advance(self):
        for i in self.matrixx():
            for j in i:
                print(j)

        matrix=self.settleMines()

        i = 0
        advanceNumber = 0

        while i < 8:
            row = int(input("Choose row for advance:"))
            if row >= 8:
                raise Exception("You cannot enter a value greater than 7 to move vertically.")
            else:
                pass

            col = int(input("Choose col for advance:"))
            if col >= 2:
                raise Exception("You cannot advance more than 2 units")
            else:
                pass
            advanceNumber += col
            self.findMine(row, col,matrix)
            matrix[0][row][advanceNumber] = "S"
            self.showArea(row,advanceNumber)
            self.findS(matrix)

            i += 1


mine=Mine()
print(mine.advance())
