from typing import Dict, List
import numpy as np


class CellMap:

	def __init__(self, cells_count: int = 10, rule: Dict[str, List[int]] = {'b': [3], 's': [2, 3]}):
		self.cells_count = cells_count
		self.map = CellMap.clear_map(self.cells_count)
		self.rule = rule


	def get_point_neighbors(self, x: int, y: int) -> np.ndarray:
		neighbors = np.zeros((8, 8)).astype(int)
		position = 0

		for i in range(x - 1, x + 2):
			for j in range(y - 1, y + 2):
				if i == x and j == y:
					continue

				if i < 0:
					neighbors[position, 0] = self.cells_count + i
				elif i > self.cells_count - 1:
					neighbors[position, 0] = i - self.cells_count
				else:
					neighbors[position, 0] = i

				if j < 0:
					neighbors[position, 1] = self.cells_count + j
				elif j > self.cells_count - 1:
					neighbors[position, 1] = j - self.cells_count
				else:
					neighbors[position, 1] = j

				position += 1

		return neighbors


	def neighbors_count(self, x: int, y: int) -> int:
		count = 0
		neighbors = self.get_point_neighbors(x, y)

		for i in range(8):
			_x = neighbors[i, 0]
			_y = neighbors[i, 1]

			if _x < 0 or _y < 0:
				continue
			if _x >= self.cells_count or _y >= self.cells_count:
				continue
			if self.map[_x, _y] == 1:
				count += 1

		return count


	def step(self):
		new_map = CellMap.clear_map(self.cells_count)

		for x in range(self.cells_count):
			for y in range(self.cells_count):
				count = self.neighbors_count(x, y)

				if self.map[x, y] == 0 and (count in self.rule['b']):
					new_map[x, y] = 1
				elif self.map[x, y] == 1 and (count in self.rule['s']):
					new_map[x, y] = 1
				else:
					new_map[x, y] = 0

		self.map = new_map


	def clear(self):
		self.map = CellMap.clear_map(self.cells_count)


	def randomize(self):
		self.map = np.random.randint(2, size=(self.cells_count, self.cells_count)).astype(int)


	@staticmethod
	def clear_map(cell_count: int) -> np.ndarray:
		return np.zeros((cell_count, cell_count)).astype(int)
