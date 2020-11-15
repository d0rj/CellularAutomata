from tkinter import *
from tkinter.filedialog import *

from cell_map import CellMap
from cell_map_widget import CellMapWidget
from serialization import serialize_cellmap, deserialize_cellmap


CELL_SIZE  = 10
CELL_COUNT = 60
STEP_INTERVAL = 100
default_rule = {'b': [3], 's': [2, 3]}
FILETYPES = [('config files', '.cfg'), ('log files', '.log')]
INSTRUMENTS_SIZE = 30


def main():
	pixels_width = CELL_COUNT * CELL_SIZE
	
	root = Tk()
	root.title('Celluar automat')
	root.geometry('{}x{}'.format(pixels_width, (pixels_width) + INSTRUMENTS_SIZE))

	f_map = Frame(root, 
					width=pixels_width, 
					height=pixels_width
					)
	f_instruments = Frame(root)

	play_icon = PhotoImage(file='.\images\play_icon.png').subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)
	next_icon = PhotoImage(file='.\images\\next_icon.png').subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)
	random_icon = PhotoImage(file='.\images\\random_icon.png').subsample(INSTRUMENTS_SIZE, INSTRUMENTS_SIZE)

	cell_map = CellMap(CELL_COUNT, default_rule)
	cell_map_widget = CellMapWidget(f_map, CELL_SIZE, STEP_INTERVAL, cell_map)

	one_step = Button(f_instruments, 
						text='Step', 
						command=cell_map_widget.step, 
						image=next_icon, 
						compound=LEFT, 
						height=INSTRUMENTS_SIZE
						)  
	clear_button = Button(f_instruments, 
							text='Clear', 
							command=cell_map_widget.on_clear, 
							height=INSTRUMENTS_SIZE
							)
	simulate_button = Button(f_instruments, 
								text='Simulate', 
								command=lambda: cell_map_widget.on_simulate(simulate_button), 
								image=play_icon, 
								compound=LEFT, 
								height=INSTRUMENTS_SIZE
								)
	random_button = Button(f_instruments, 
							text='Random', 
							command=cell_map_widget.on_randomize, 
							image=random_icon, 
							compound=LEFT, 
							height=INSTRUMENTS_SIZE
							)
	log_button = Button(f_instruments, 
						text='Log', 
						command=lambda: cell_map_widget.on_log(log_button), 
						height=INSTRUMENTS_SIZE
						)

	main_menu = Menu()

	file_menu = Menu(main_menu)
	file_menu.add_command(
		label='Open',
		command=(
			lambda: 
			cell_map_widget.on_set_config(deserialize_cellmap(askopenfilename(
				initialdir='/', title='Select config', filetypes=FILETYPES
			)) or CellMap.clear_map(CELL_COUNT))
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

	map_config_menu = Menu(main_menu)
	map_config_menu.add_command(
		label='Planner gun', 
		command=(
			lambda: cell_map_widget.on_set_config(deserialize_cellmap('map_configs/planner.cfg'))
			)
	)

	main_menu.add_cascade(label='File', menu=file_menu)
	main_menu.add_cascade(label='Map Config', menu=map_config_menu)

	simulate_button.pack(side=LEFT)
	one_step.pack(side=LEFT)
	clear_button.pack(side=LEFT)
	random_button.pack(side=LEFT)
	log_button.pack(side=LEFT)

	f_map.pack(fill=X, side=BOTTOM)
	f_instruments.pack(fill=X, side=TOP)

	root.config(menu=main_menu)
	root.mainloop()


if __name__ == '__main__':
	main()
