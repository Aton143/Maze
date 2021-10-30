from UnionFind import UnionFind
import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[1] * (2 * cols - 1) for i in range(2 * rows - 1)]
        self.coorStack = []
        self.coorSet = set()

        for i in range(rows):
            for j in range(cols):
                self.matrix[2*i][2*j] = 0
                self.coorStack.append((i, j))

        random.shuffle(self.coorStack)

    def printMaze(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def numCols(self):
        return 2 * self.cols - 1
    def numRows(self):
        return 2 * self.rows - 1
    def accessMatrix(self, i, j):
        return self.matrix[i][j]

    def kruskal(self):
        unionFind = UnionFind(self.rows * self.cols)
        choices = []
        def createChoices(i, j):
            choices = []
            if i + 1 < self.rows:
                choices.append((i + 1, j))
            if j + 1 < self.cols:
                choices.append((i, j + 1))
            random.shuffle(choices)
            return choices
        while unionFind.components() > 1 and self.coorStack:
            coord = self.coorStack.pop()
            if coord in self.coorSet:
                continue
            else:
                self.coorSet.add(coord)
                i = coord[0]
                j = coord[1]
                choices = createChoices(i, j)
                cur_choice = ()

                while len(choices) > 0:
                    cur_choice = choices.pop()
                    if cur_choice not in self.coorSet:
                        break
                if cur_choice:
                    coord_conv = coord[0] * self.rows + coord[1]
                    choice_conv = cur_choice[0] * self.rows + cur_choice[1]
                    unionFind.unify(coord_conv, choice_conv)

                    if cur_choice[0] != i:
                        self.matrix[2 * i + 1][2 * j] = 0
                    else:
                        self.matrix[2 * i][2 * j + 1] = 0