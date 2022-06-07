#!/usr/bin/python3
'''0x09. Island Perimeter'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid)
    lst_max = len(grid[0])

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:
                # left side
                if lst[land_idx - 1] == 0:
                    counter += 1

                # top side
                if grid[lst_idx - 1][land_idx] == 0:
                    counter += 1

                # right side
                if lst[land_idx - 1] == 0:
                    counter += 1

                # bottom side
                if grid[lst_idx + 1][land_idx] == 0:
                    counter += 1

    return counter
