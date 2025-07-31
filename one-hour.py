dead = " "
live = "+"

def print_grid(grid, generation = 0):
    print("------------------ Gen: " + str(generation) + " ------------------")
    print("", end="\t")
    for cell in grid[0]:
        print("↓", end="\t")
    print()
    for row in grid:
        print("→", end="\t")
        for cell in row:
            print(cell, end="\t")
        print()


def calc_live_neighbors(grid, i, j):
    liveCount = 0
    if i > 0 and j > 0 and grid[i-1][j-1] == live:
        liveCount += 1
    if i > 0 and grid[i-1][j] == live:
        liveCount += 1
    if j > 0 and grid[i][j-1] == live:
        liveCount += 1
    if i < len(grid)-1 and grid[i+1][j] == live:
        liveCount += 1
    if j < len(grid[i])-1 and grid[i][j+1] == live:
        liveCount += 1 
    if i < len(grid)-1 and j < len(grid[i])-1 and grid[i+1][j+1] == live:
        liveCount += 1
    if i > 0 and j < len(grid[i])-1 and grid[i-1][j+1] == live:
        liveCount += 1 
    if i < len(grid)-1 and j > 0 and grid[i+1][j-1] == live:
        liveCount += 1
    return liveCount


def next_gen(grid):
    result = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            n = calc_live_neighbors(grid, i, j)
            if grid[i][j] == live:
                if n < 2:
                    result[i][j] = dead
                elif n > 3:
                    result[i][j] = dead
            else:
                if n == 3:
                    result[i][j] = live
    return result


def init_grid_L(grid, offset = 0):
    if len(grid) < offset + 2:
        print("(!) Can't make init_grid_L")
        return grid
    grid[offset+0][offset+0] = live
    grid[offset+0][offset+1] = live
    grid[offset+1][offset+1] = live
    return grid

def init_grid_glider(grid, offset = 0):
    if len(grid) < offset + 3:
        print("(!) Can't make init_grid_glider")
        return grid
    grid[offset+0][offset+1] = live
    grid[offset+1][offset+2] = live
    grid[offset+2][offset+0] = live
    grid[offset+2][offset+1] = live
    grid[offset+2][offset+2] = live
    return grid

def main():
    print("Please input the width of the active board:")
    width = int(input())
    print("Please input the number of generations needed:")
    generations = int(input())
    if width < 0 or generations < 0:
        print("Invalid inputs")
        return
    print("Building Game of life with " + str(width) + " cols and rows.")
    
    grid = [[dead for x in range(width)] for y in range(width)]

    grid = init_grid_glider(grid, 2)
    print_grid(grid)
    
    for g in range(generations):
        grid = next_gen(grid)
        print_grid(grid, g + 1)



if __name__ == "__main__":
    main()
