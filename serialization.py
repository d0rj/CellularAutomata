import numpy as np


def serialize_cellmap_only(cellmap: np.ndarray, width: int, height: int, file_name: str):
	with open(file_name, 'a+') as file:
		file.write('{0} {1}\n'.format(width, height))
		for y in range(height):
			num = 0
			mul = 1

			for x in range(width):
				num += mul * cellmap[y, x]
				mul *= 2

			file.write('{} '.format(num))
			
		file.write('\n')


def serialize_cellmap(cellmap: np.ndarray, file_name: str):
	width = len(cellmap[0])
	height = len(cellmap)

	serialize_cellmap_only(cellmap, width, height, file_name)


def deserialize_cellmap_only(width: int, height: int, opened_file) -> np.ndarray:
	nums = [int(num) for num in opened_file.readline().split(' ') if num != '\n']
	cellmap = np.zeros((height, width)).astype(int)

	for y in range(height):
		for x in range(width):
			cellmap[y, x] = nums[y] % 2
			nums[y] //= 2

	return cellmap


def deserialize_cellmap(file_name: str) -> np.ndarray:
	try:
		file = open(file_name, 'r')
	except Exception:
		return None
	
	width, height = [int(num) for num in file.readline().split(' ')]

	result = deserialize_cellmap_only(width, height, file)
	if result.any():
		return result
	else:
		return np.zeros((height, width)).astype(int)
