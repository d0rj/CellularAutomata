from tkinter import Frame, Canvas, TOP
import numpy as np

from cell_map import CellMap
from logger import Logger


class CellMapWidget(Frame):

	def __init__(self, master, cell_size: int, step_interval: int, cell_map: CellMap):
		self.cell_size = cell_size
		self.step_interval = step_interval
		self.cell_map = cell_map
		self.simulating = False
		self.logging = False

		self.canvas = Canvas(
			master, 
			width=(self.cell_map.cells_count * cell_size),
			height=(self.cell_map.cells_count * cell_size),
			bg='white'
			)
		self.canvas.pack(side=TOP)
		self.canvas.bind('<Button-1>', self._on_click)

		self.draw()


	def draw(self):
		self.draw_grid()
		self.draw_map()
		

	def _on_click(self, event):
		x, y = event.x // self.cell_size, event.y // self.cell_size
		self.cell_map.map[x, y] = (self.cell_map.map[x, y] + 1) % 2

		self.canvas.delete('all')
		self.draw()


	def draw_cell(self, x: int, y: int):
		cell_size = self.cell_size

		self.canvas.create_rectangle(
			cell_size * x,
			cell_size * y, 
			cell_size * (x + 1), 
			cell_size * (y + 1), 
			fill='black'
			)


	def draw_grid(self):
		draw_line_func = self.canvas.create_line
		cells_count = self.cell_map.cells_count
		cell_size = self.cell_size

		for i in range(0, cells_count * cell_size, cell_size):
			draw_line_func(0, i, cells_count * cell_size, i)

		for i in range(0, cells_count * cell_size, cell_size):
			draw_line_func(i, 0, i, cells_count * cell_size)


	def draw_map(self):
		draw_cell_func = self.draw_cell
		cells_count = self.cell_map.cells_count
		map_ = self.cell_map.map

		for i in range(cells_count):
			for j in range(cells_count):
				if map_[i, j] == 1:
					draw_cell_func(i, j)


	def step(self):
		self.canvas.delete('all')

		self.cell_map.step()

		if self.logging:
			self.logger.log(self.cell_map.map)

		self.draw()


	def simulate_loop(self):
		if self.simulating:
			self.step()
			self.canvas.after(self.step_interval, self.simulate_loop)


	def on_simulate(self, indicator):
		self.simulating = not self.simulating
		self.simulate_loop()

		if indicator:
			if self.simulating:
				indicator.configure(bg='red')
			else:
				indicator.configure(bg='white')


	def on_randomize(self):
		self.canvas.delete('all')

		self.cell_map.randomize()

		if self.logging:
			self.logger.log(self.cell_map.map)

		self.draw()


	def on_clear(self):
		self.canvas.delete('all')

		self.cell_map.clear()

		if self.logging:
			self.logger.log(self.cell_map.map)

		self.draw()


	def on_set_config(self, new_map: np.ndarray):
		self.canvas.delete('all')

		self.cell_map.map = new_map

		if self.logging:
			self.logger.log(self.cell_map.map)

		self.draw()


	def on_start_log(self, session_name: str = 'default'):
		self.logging = True
		self.logger = Logger()
		self.logger.start_session(self.cell_map.map, session_name)


	def on_end_log(self):
		self.logger.end_session()
		self.logging = False


	def on_log(self, indicator, session_name: str = 'default'):
		if not self.logging:
			indicator.configure(bg='red')
			self.on_start_log(session_name)
		else:
			indicator.configure(bg='white')
			self.on_end_log()
