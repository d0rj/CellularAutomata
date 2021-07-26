from tkinter import Tk, Frame, PhotoImage, Button, Menu, Entry, Label,\
    X, LEFT, BOTTOM, TOP
from tkinter.constants import RIGHT
from tkinter.filedialog import asksaveasfilename, askopenfilename
from os import listdir

from cell_map import CellMap
from cell_map_widget import CellMapWidget
from serialization import serialize_cellmap, deserialize_cellmap


CELL_SIZE = 10
CELL_COUNT = 60
STEP_INTERVAL = 50
DEFAULT_RULE = {'b': [3], 's': [2, 3]}
FILETYPES = [('config files', '.cfg'), ('log files', '.log')]
INSTRUMENTS_SIZE = 30


def input_to_list(string: str) -> list:
    string.replace(',', ' ')
    return [int(num) for num in string.split()]


def main():
    pixels_width = CELL_COUNT * CELL_SIZE

    root = Tk()
    root.title('Cellular automata (Game of life version)')
    root.geometry(f'{pixels_width}x{pixels_width + INSTRUMENTS_SIZE}')
    root.resizable(False, False)

    f_map = Frame(
        root,
        width=pixels_width,
        height=pixels_width
        )
    f_instruments = Frame(root)

    play_icon = PhotoImage(file='.\\images\\play_icon.png')\
        .subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)
    next_icon = PhotoImage(file='.\\images\\next_icon.png')\
        .subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)
    random_icon = PhotoImage(file='.\\images\\random_icon.png')\
        .subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)

    cell_map = CellMap(CELL_COUNT, DEFAULT_RULE)
    cell_map_widget = CellMapWidget(f_map, CELL_SIZE, STEP_INTERVAL, cell_map)

    one_step = Button(
        f_instruments,
        text='Step',
        command=cell_map_widget.step,
        image=next_icon,
        compound=LEFT,
        height=INSTRUMENTS_SIZE
        )
    clear_button = Button(
        f_instruments,
        text='Clear',
        command=cell_map_widget.on_clear,
        height=INSTRUMENTS_SIZE
        )
    simulate_button = Button(
        f_instruments,
        text='Simulate',
        command=lambda: cell_map_widget.on_simulate(simulate_button),
        image=play_icon,
        compound=LEFT,
        height=INSTRUMENTS_SIZE
        )
    random_button = Button(
        f_instruments,
        text='Random',
        command=cell_map_widget.on_randomize,
        image=random_icon,
        compound=LEFT,
        height=INSTRUMENTS_SIZE
        )
    log_button = Button(
        f_instruments,
        text='Log',
        command=lambda: cell_map_widget.on_log(log_button),
        height=INSTRUMENTS_SIZE
        )

    birth_entry = Entry(f_instruments, width=10)
    birth_entry.insert(0, DEFAULT_RULE['b'])
    birth_label = Label(f_instruments, text='Birth:')
    survive_entry = Entry(f_instruments, width=10)
    survive_entry.insert(0, DEFAULT_RULE['s'])
    survive_label = Label(f_instruments, text='Survive:')

    configure_button = Button(
        f_instruments,
        text='Configure',
        command=lambda: cell_map.set_rule({
                'b': input_to_list(birth_entry.get()),
                's': input_to_list(survive_entry.get())
            })
    )

    main_menu = Menu()

    file_menu = Menu(main_menu)
    file_menu.add_command(
        label='Open..',
        command=(
            lambda:
            cell_map_widget.on_set_config(
                deserialize_cellmap(
                    askopenfilename(
                        initialdir='/',
                        title='Select config',
                        filetypes=FILETYPES
                        )
                    )
                )
        )
    )
    file_menu.add_command(
        label='Save...',
        command=(
            lambda:
            serialize_cellmap(
                cell_map_widget.cell_map.map,
                asksaveasfilename(
                    filetypes=FILETYPES,
                    defaultextension='.cfg'
                ) or './default.cfg'
            )
        )
    )

    def set_config_handler_build(arg):
        return lambda: cell_map_widget.on_set_config(
            deserialize_cellmap(f'./map_configs/{arg}')
        )

    map_config_menu = Menu(main_menu)
    for filename in listdir('./map_configs/'):
        if filename.endswith('.cfg'):
            map_config_menu.add_command(
                label=filename[:-4].capitalize(),
                command=set_config_handler_build(filename)
            )

    main_menu.add_cascade(label='File', menu=file_menu)
    main_menu.add_cascade(label='Map Config', menu=map_config_menu)

    simulate_button.pack(side=LEFT)
    one_step.pack(side=LEFT)
    clear_button.pack(side=LEFT)
    random_button.pack(side=LEFT)
    log_button.pack(side=LEFT)

    configure_button.pack(side=RIGHT)
    survive_entry.pack(side=RIGHT)
    survive_label.pack(side=RIGHT)
    birth_entry.pack(side=RIGHT)
    birth_label.pack(side=RIGHT)

    f_map.pack(fill=X, side=BOTTOM)
    f_instruments.pack(fill=X, side=TOP)

    root.config(menu=main_menu)
    root.mainloop()


if __name__ == '__main__':
    main()
