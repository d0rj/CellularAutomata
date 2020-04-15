from tkinter import *
from typing import List
import time
from CellMap import CellMap
from CellMapWidget import CellMapWidget


CELL_SIZE  = 10
CELL_COUNT = 60
STEP_INTERVAL = 100
rule = {'b': [3], 's': [2, 3]}


def planner_gun() -> List[List[int]]:
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

    return card


def main():    
    root = Tk()
    root.title('Celluar automat')
    root.geometry('700x700')
    f_top = Frame(root)
    f_bot = Frame(root)

    cell_map = CellMap(CELL_COUNT, rule)
    cell_map_widget = CellMapWidget(root, CELL_SIZE, STEP_INTERVAL, cell_map)

    f_top.pack(side=TOP)
    f_bot.pack(side=BOTTOM)
    one_step = Button(f_bot, text='Step', command=cell_map_widget.step)  
    clear_button = Button(f_bot, text='Clear', command=cell_map_widget.on_clear)
    simulate_button = Button(f_bot, text='Simulate', command=cell_map_widget.on_simulate)
    random_button = Button(f_bot, text='Random', command=cell_map_widget.on_randomize)

    main_menu = Menu()
    config_menu = Menu()
    config_menu.add_command(label='Planner gun', command=(lambda: cell_map_widget.on_set_config(planner_gun())))

    main_menu.add_cascade(label='Config', menu=config_menu)

    one_step.pack(side=LEFT)
    clear_button.pack(side=RIGHT)
    simulate_button.pack(side=BOTTOM)
    random_button.pack(side=BOTTOM)

    root.config(menu=main_menu)
    root.mainloop()


if __name__ == '__main__':
    main()