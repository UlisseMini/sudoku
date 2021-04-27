def show_box(box: list) -> str:
    for i in range(len(box)):
        for j in range(len(box[i])):
            print(box[i][j], end=' ')
        print()


class Grid:
    """
    A sudoku grid of size n (where n is a multiple of 3),
    0 represents an empty square.
    """

    def __init__(self, n=9):
        assert n % 3 == 0
        self.n = n
        self.n_boxes = n // 3
        self.grid = [
            [0] * n
            for _ in range(n)
        ]


    def box(self, i, j):
        "Return the box at (i,j) (box coordinates)"
        x,y = i*3, j*3
        box = [[0] * 3 for _ in range(3)]
        for dx in range(3):
            for dy in range(3):
                box[dx][dy] = self.grid[x + dx][y + dy]
        return box


    def boxes(self):
        "Iterator over all boxes from top left to bottom right"
        for i in range(self.n_boxes):
            for j in range(self.n_boxes):
                yield self.box(i,j)


    def rows(self):
        return self.grid


    def cols(self):
        xs = []
        for j in range(self.n):
            xs.append([self.grid[i][j] for i in range(self.n)])
        return xs

    def legal(self):
        "Is the current position legal?"

        def duplicate(lst: list) -> bool:
            for i in range(1, 10):
                if lst.count(i) > 1:
                    return True
            return False


        # 1. Every box should have at most 1 of each number
        for box in self.boxes():
            flat = [item for row in box for item in row]
            if duplicate(flat):
                return False

        # 2. Every row should have at most 1 of each number
        for row in self.rows():
            if duplicate(row):
                return False

        # 3. Every col should have at most 1 of each number
        for col in self.cols():
            if duplicate(col):
                return False

        return True


    def __str__(self):
        "String for an (n by n) grid"

        s = ''
        for i,row in enumerate(self.grid):
            for j,item in enumerate(row):
                s += f'{item}{" " if (j+1)%3 != 0 else "|"}'
            s += '\n' if (i+1)%3 != 0 else '\n' + '-' * self.n*2 + '\n'

        return s

if __name__ == '__main__':
    grid = Grid()

    grid.grid[0][1] = 2
    # grid.grid[0][1] = 1

    grid.grid[5][1] = 2
    # grid.grid[0][6] = 2

    print(grid)
    assert grid.legal() == False
