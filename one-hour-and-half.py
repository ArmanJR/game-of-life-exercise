DEAD = " "
LIVE = "+"

def print_grid(grid, generation=0):
    if not grid:
        print("(empty grid)")
        return
    print(f"------ Generation {generation} ------")
    for row in grid:
        print("".join(row))
    print()


def calc_live_neighbors(grid, i, j):
    offsets = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,-1), (1,1)]
    count = 0
    for di, dj in offsets:
        ni, nj = i+di, j+dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == LIVE:
            count += 1
    return count


def next_gen(grid):
    result = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            n = calc_live_neighbors(grid, i, j)
            if grid[i][j] == LIVE:
                if n < 2:
                    result[i][j] = DEAD
                elif n > 3:
                    result[i][j] = DEAD
            else:
                if n == 3:
                    result[i][j] = LIVE
    return result


def init_grid_L(grid, offset = 0):
    if len(grid) < offset + 2:
        raise ValueError("Grid too small for L")
    grid[offset+0][offset+0] = LIVE
    grid[offset+0][offset+1] = LIVE
    grid[offset+1][offset+1] = LIVE
    return grid


def init_grid_glider(grid, offset = 0):
    if len(grid) < offset + 3:
        raise ValueError("Grid too small for glider")
    pattern = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dr, dc in pattern:
        grid[offset+dr][offset+dc] = LIVE


def main():
    try:
        width = int(input("Board width (greater than 1): "))
        gens = int(input("Generations (greater than 0): "))
        if width < 1 or gens < 0:
            raise ValueError
    except ValueError:
        print("Width must be >= 1 and generations >= 0.")
        return
    
    grid = [[DEAD] * width for _ in range(width)]

    init_grid_glider(grid, 2)
    print_grid(grid)
    
    for g in range(gens):
        grid = next_gen(grid)
        print_grid(grid, g + 1)


if __name__ == "__main__":
    main()
