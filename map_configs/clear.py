from typing import List


def clear_map(cell_count: int) -> List[List[int]]:
    return [[0 for j in range(cell_count)] for i in range(cell_count)]
    