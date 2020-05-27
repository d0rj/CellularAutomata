from tkinter import *
from tkinter.filedialog import *

from cell_map import CellMap
from cell_map_widget import CellMapWidget
from map_configs.clear import clear_map
from serialization import serialize_cellmap, deserialize_cellmap


CELL_SIZE  = 10
CELL_COUNT = 60
STEP_INTERVAL = 100
default_rule = {'b': [3], 's': [2, 3]}
FILETYPES = [('config files', '.cfg'), ('log files', '.log')]


def main():
    root = Tk()
    root.title('Celluar automat')
    root.geometry('600x700')
    f_top = Frame(root, width=(CELL_COUNT * CELL_SIZE), height=(CELL_COUNT * CELL_SIZE))
    f_bot = Frame(root)

    play_icon = PhotoImage(file='.\images\play_icon.png').subsample(30, 30)
    next_icon = PhotoImage(file='.\images\\next_icon.png').subsample(30, 30)
    random_icon = PhotoImage(file='.\images\\random_icon.png').subsample(30, 30)

    cell_map = CellMap(CELL_COUNT, default_rule)
    cell_map_widget = CellMapWidget(f_top, CELL_SIZE, STEP_INTERVAL, cell_map)

    f_top.pack(fill=X, side=TOP)
    f_bot.pack(fill=X, side=BOTTOM)
    one_step = Button(f_bot, text='Step', command=cell_map_widget.step, image=next_icon, compound=LEFT)  
    clear_button = Button(f_bot, text='Clear', command=cell_map_widget.on_clear)
    simulate_button = Button(f_bot, text='Simulate', command=lambda: cell_map_widget.on_simulate(simulate_button), image=play_icon, compound=LEFT)
    random_button = Button(f_bot, text='Random', command=cell_map_widget.on_randomize, image=random_icon, compound=LEFT)
    log_button = Button(f_bot, text='Log', command=lambda: cell_map_widget.on_log(log_button))

    main_menu = Menu()

    file_menu = Menu()
    file_menu.add_command(
        label='Open',
        command=(
            lambda: 
            cell_map_widget.on_set_config(deserialize_cellmap(askopenfilename(
                initialdir='/', title='Select config', filetypes=FILETYPES
            )) or clear_map(CELL_COUNT))
        )
    )
    file_menu.add_command(
        label='Create',
        command=(
            lambda: 
            serialize_cellmap(
                cell_map_widget.cell_map.map, 
                asksaveasfilename(filetypes=FILETYPES, defaultextension='.cfg') or './default.cfg'
            )
        )
    )

    config_menu = Menu()
    config_menu.add_command(
        label='Planner gun', 
        command=(
            lambda: cell_map_widget.on_set_config(deserialize_cellmap('map_configs/planner.cfg'))
            )
    )

    main_menu.add_cascade(label='File', menu=file_menu)
    main_menu.add_cascade(label='Config', menu=config_menu)

    one_step.pack(side=LEFT)
    clear_button.pack(side=RIGHT)
    simulate_button.pack(side=BOTTOM)
    random_button.pack(side=BOTTOM)
    log_button.pack(side=BOTTOM)

    root.config(menu=main_menu)
    root.mainloop()


if __name__ == '__main__':
    main()