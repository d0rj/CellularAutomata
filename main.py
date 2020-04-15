from tkinter import *
from typing import List
import time
from cell_map import CellMap
from cell_map_widget import CellMapWidget
from map_configs.planner_gun import planner_gun


CELL_SIZE  = 10
CELL_COUNT = 60
STEP_INTERVAL = 100
rule = {'b': [3], 's': [2, 3]}


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
    config_menu.add_command(label='Planner gun', command=(lambda: cell_map_widget.on_set_config(planner_gun(CELL_COUNT))))

    main_menu.add_cascade(label='Config', menu=config_menu)

    one_step.pack(side=LEFT)
    clear_button.pack(side=RIGHT)
    simulate_button.pack(side=BOTTOM)
    random_button.pack(side=BOTTOM)

    root.config(menu=main_menu)
    root.mainloop()


if __name__ == '__main__':
    main()