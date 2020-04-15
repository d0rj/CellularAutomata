from tkinter import *


class CellMap():

    def __init__(self, master):
        self.CELL_SIZE  = 10
        self.CELL_COUNT = 60
        self.card = [[0 for j in range(self.CELL_COUNT)] for i in range(self.CELL_COUNT)]
        self.c = Canvas(master, width=(CELL_COUNT * CELL_SIZE), height=(CELL_COUNT * CELL_SIZE), bg='white')


    def draw_grid(self):
        for i in range(0, self.CELL_COUNT * self.CELL_SIZE, self.CELL_SIZE):
            self.c.create_line(0, i, self.CELL_COUNT * self.CELL_SIZE, i)

        for i in range(0, self.CELL_COUNT * self.CELL_SIZE, self.CELL_SIZE):
            self.c.create_line(i, 0, i, self.CELL_COUNT * self.CELL_SIZE)


    def draw_cell(self, x: int, y: int):
        self.c.create_rectangle(self.CELL_SIZE * x, self.CELL_SIZE * y, \
            self.CELL_SIZE * (x+1), self.CELL_SIZE * (y+1), fill='black')


    def read_point_neighbors(self, x: int, y: int):
        nb = [[0, 0]for i in range(8)]
        i = 0
        j = 0
        k = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                nb[k][0] = i
                nb[k][1] = j
                k += 1

        return nb


    def neighbors_count(self, x: int, y: int):
        sum = 0
        nb = self.read_point_neighbors(x, y)

        for i in range(8):
            _x = nb[i][0]
            _y = nb[i][1]

            if _x < 0 or _y < 0:
                continue
            if _x >= self.CELL_COUNT or _y >= self.CELL_COUNT:
                continue
            if self.card[_x][_y] == 1:
                sum += 1

        return sum


    def draw_map(self):
        for i in range(self.CELL_COUNT):
            for j in range(self.CELL_COUNT):
                if self.card[i][j] == 1:
                    self.draw_cell(i, j)


    def step(self):
        self.c.delete('all')
        self.draw_grid()

        new_card = [[0 for j in range(self.CELL_COUNT)] for i in range(self.CELL_COUNT)]

        for x in range(self.CELL_COUNT):
            for y in range(self.):
                count = self.neighbors_count(x, y)
                if self.card[x][y] == 0 and count == 3:
                    new_card[x][y] = 1
                elif self.card[x][y] == 1 and (count < 2 or count > 3):
                    new_card[x][y] = 0
                elif self.card[x][y] == 1 and (count == 2 or count == 3):
                    new_card[x][y] = 1

        self.card = new_card

        self.draw_map()


    def on_click(event):
        x, y = event.x // 10, event.y // 10
        self.card[x][y] = (self.card[x][y] + 1) % 2
        self.draw_map()
