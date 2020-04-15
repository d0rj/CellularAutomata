from tkinter import *
import time
import random


CELL_SIZE  = 10
CELL_COUNT = 60
SIMULATING = False
STEP_INTERVAL = 100
rule = {'b': [3], 's': [2, 3]}

card = [[0 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]

root = None
c = None
solve = None


def read_point_neighbors(x: int, y: int):
    nb = [[0, 0]for i in range(8)]
    k = 0

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue

            if i < 0:
                nb[k][0] = CELL_COUNT + i
            elif i > CELL_COUNT - 1:
                nb[k][0] = i - CELL_COUNT
            else:
                nb[k][0] = i

            if j < 0:
                nb[k][1] = CELL_COUNT + j
            elif j > CELL_COUNT - 1:
                nb[k][1] = j - CELL_COUNT
            else:
                nb[k][1] = j
                
            k += 1

    return nb


def neighbors_count(x: int, y: int):
    sum = 0
    nb = read_point_neighbors(x, y)

    for i in range(8):
        _x = nb[i][0]
        _y = nb[i][1]

        if _x < 0 or _y < 0:
            continue
        if _x >= CELL_COUNT or _y >= CELL_COUNT:
            continue
        if card[_x][_y] == 1:
            sum += 1

    return sum


def draw_grid():
    global c
    for i in range(0, CELL_COUNT * CELL_SIZE, CELL_SIZE):
        c.create_line(0, i, CELL_COUNT * CELL_SIZE, i)

    for i in range(0, CELL_COUNT * CELL_SIZE, CELL_SIZE):
        c.create_line(i, 0, i, CELL_COUNT * CELL_SIZE)


def draw_cell(x: int, y: int):
    global c
    c.create_rectangle(CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE * (x+1), CELL_SIZE * (y+1), fill='black')


def draw_map():
    global c
    for i in range(CELL_COUNT):
        for j in range(CELL_COUNT):
            if card[i][j] == 1:
                draw_cell(i, j)


def step():
    global card
    global c

    c.delete('all')
    draw_grid()

    new_card = [[0 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]

    for x in range(CELL_COUNT):
        for y in range(CELL_COUNT):
            neighbors = neighbors_count(x, y)

            if card[x][y] == 0:
                for birth in rule['b']:
                    if neighbors == birth:
                        new_card[x][y] = 1
                        break
            elif card[x][y] == 1:
                surv = False
                for survival in rule['s']:
                    if neighbors == survival:
                        new_card[x][y] = 1
                        surv = True
                        break

                if not surv:
                    new_card[x][y] = 0

    card = new_card

    draw_map()


def on_click(event):
    global c
    x, y = event.x // 10, event.y // 10
    card[x][y] = (card[x][y] + 1) % 2
    c.delete('all')
    draw_grid()
    draw_map()


def clear():
    global c
    global card

    c.delete('all')
    card = [[0 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]
    draw_grid()
    draw_map()


def simulate():
    global c
    global root
    global SIMULATING
    global solve

    SIMULATING = not SIMULATING
    simulate_loop()


def simulate_loop():
    global root
    global SIMULATING
    global STEP_INTERVAL

    if SIMULATING:
        step()
        root.after(STEP_INTERVAL, simulate_loop)


def randomize():
    global card
    global c

    c.delete('all')
    card = [[random.randint(0, 1) for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]
    draw_grid()
    draw_map()


def planner_gun():
    global card
    global c

    c.delete('all')
    card = [[0 for j in range(CELL_COUNT)] for i in range(CELL_COUNT)]
    card[1][8] = 1
    card[1][9] = 1
    card[2][8] = 1
    card[2][9] = 1

    card[11][7] = 1
    card[11][8] = 1
    card[11][9] = 1
    card[12][6] = 1
    card[12][10] = 1
    card[13][5] = 1
    card[14][5] = 1
    card[13][11] = 1
    card[14][11] = 1
    card[15][8] = 1
    card[16][6] = 1
    card[16][10] = 1
    card[17][7] = 1
    card[17][8] = 1
    card[17][9] = 1
    card[18][8] = 1

    card[21][5] = 1
    card[21][6] = 1
    card[21][7] = 1
    card[22][5] = 1
    card[22][6] = 1
    card[22][7] = 1
    card[23][4] = 1
    card[23][8] = 1
    card[25][3] = 1
    card[25][4] = 1
    card[25][8] = 1
    card[25][9] = 1

    card[35][5] = 1
    card[35][6] = 1
    card[36][5] = 1
    card[36][6] = 1

    draw_grid()
    draw_map()


def start_pos():
    pass


def main():
    global root
    global c
    
    root = Tk()
    root.title('Клеточный автомат')
    root.geometry('700x700')
    f_top = Frame(root)
    f_bot = Frame(root)

    c = Canvas(f_top, width=(CELL_COUNT * CELL_SIZE), height=(CELL_COUNT * CELL_SIZE), bg='white')

    f_top.pack(side=TOP)
    f_bot.pack(side=BOTTOM)
    one_step = Button(f_bot, text='Step', command=step)  
    clear_button = Button(f_bot, text='Clear', command=clear)
    simulate_button = Button(f_bot, text='Simulate', command=simulate)
    random_button = Button(f_bot, text='Random', command=randomize)

    main_menu = Menu()
    config_menu = Menu()
    config_menu.add_command(label='Планерное ружьё', command=planner_gun)

    main_menu.add_cascade(label='Config', menu=config_menu)

    one_step.pack(side=LEFT)
    clear_button.pack(side=RIGHT)
    simulate_button.pack(side=BOTTOM)
    random_button.pack(side=BOTTOM)
    c.pack(side=LEFT)

    c.bind('<Button-1>', on_click)

    draw_grid()
    start_pos()
    draw_map()

    root.config(menu=main_menu)
    root.mainloop()


if __name__ == '__main__':
    main()