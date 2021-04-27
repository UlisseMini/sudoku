import sudoku
import time

# yes this is ugly who cares
def backtracking(grid: sudoku.Grid) -> bool:
    if grid.legal() == False:
        return False

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1, 10):
                    grid[i][j] = k
                    if backtracking(grid):
                        return True
                    else:
                        grid[i][j] = 0

            # if its still zero all our options failed and we must backtrack.
            if grid[i][j] == 0:
                return False

    return True


def test(grid, solver):
    print(grid)

    start = time.monotonic()
    solved = solver(grid)
    took = time.monotonic() - start

    print(f'took: {took:.3f}s solved: {solved}')
    print(grid)


if __name__ == '__main__':
    # adverserial sudoku to the dumb algorithm (from wikipedia)
    s = "000000000000003085001020000000507000004000100090000000500000073002010000000040009"
    print(len(s))
    grid = sudoku.from_str(s)
    test(grid, backtracking)
    print('steps', steps)

