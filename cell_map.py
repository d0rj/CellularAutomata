from typing import Dict, List
from copy import deepcopy

import numpy as np


class CellMap:
    __slots__ = ('cells_count', 'rule', 'map', 'next_map')


    def __init__(self, cells_count: int, rule: Dict[str, List[int]]):
        self.cells_count = cells_count
        self.map = np.zeros((cells_count, cells_count)).astype(int)
        self.next_map = deepcopy(self.map)
        self.rule = rule


    def _get_point_neighbors(self, x: int, y: int) -> np.ndarray:
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


    def _neighbors_count(self, x: int, y: int) -> int:
        count = 0
        neighbors = self._get_point_neighbors(x, y)

        for i in range(8):
            _x = neighbors[i, 0]
            _y = neighbors[i, 1]

            if self.map[_x, _y] == 1:
                count += 1

        return count


    def step(self):
        count_func = self._neighbors_count
        cells_count = self.cells_count
        rule = self.rule

        for x in range(cells_count):
            for y in range(cells_count):
                count = count_func(x, y)

                if self.map[x, y] == 0 and (count in rule['b']):
                    self.next_map[x, y] = 1
                elif self.map[x, y] == 1 and (count in rule['s']):
                    self.next_map[x, y] = 1
                else:
                    self.next_map[x, y] = 0

        self.map = self.next_map.copy()
        self.next_map.fill(0)


    def clear(self):
        self.map.fill(0)


    def randomize(self):
        self.map = np.random.randint(2, size=(self.cells_count, self.cells_count)).astype(int)


    def set_rule(self, new_rule: dict):
        self.rule = new_rule
