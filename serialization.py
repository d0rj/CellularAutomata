from typing import List


def serialize_cellmap(cellmap: List[List[int]], file_name: str):
    width = len(cellmap[0])
    height = len(cellmap)

    with open(file_name, 'w+') as file:
        file.write('{0} {1}\n'.format(width, height))

        for y in range(height):
            num = 0
            mul = 1

            for x in range(width):
                num += mul * cellmap[y][x]
                mul *= 2

            file.write('{} '.format(num))
            
        file.write('\n')


def deserialize_cellmap(file_name: str) -> List[List[int]]:
    file = open(file_name, 'r')

    width, height = [int(num) for num in file.readline().split(' ')]

    nums = [int(num) for num in file.readline().split(' ') if num != '\n']
    cellmap = [[0 for i in range(width)] for j in range(height)]
    for y in range(height):
        mul = 2**width

        for x in range(width):
            cellmap[y][x] = nums[y] % 2
            nums[y] //= 2

    return cellmap
