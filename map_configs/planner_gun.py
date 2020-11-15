from typing import List


def planner_gun(cell_count: int) -> List[List[int]]:
	card = [[0 for j in range(cell_count)] for i in range(cell_count)]
	card[1][8] = 1
	card[1][9] = 1
	card[2][8] = 1
	card[2][9] = 1

	card[11][7] = 1
	card[11][8] = 1
	card[11][9] = 1
	card[12][6] = 1
	card[12][10] = 1
	card[13][5] = 1
	card[14][5] = 1
	card[13][11] = 1
	card[14][11] = 1
	card[15][8] = 1
	card[16][6] = 1
	card[16][10] = 1
	card[17][7] = 1
	card[17][8] = 1
	card[17][9] = 1
	card[18][8] = 1

	card[21][5] = 1
	card[21][6] = 1
	card[21][7] = 1
	card[22][5] = 1
	card[22][6] = 1
	card[22][7] = 1
	card[23][4] = 1
	card[23][8] = 1
	card[25][3] = 1
	card[25][4] = 1
	card[25][8] = 1
	card[25][9] = 1

	card[35][5] = 1
	card[35][6] = 1
	card[36][5] = 1
	card[36][6] = 1

	return card
