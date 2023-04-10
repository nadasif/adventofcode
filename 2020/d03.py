from lib.mylib import loadData


def count_trees(grid, right: int, down: int) -> int:
    row, col, trees = 0, 0, 0
    while True:
        col = (col + right) % len(grid[row])
        row += down
        if row > len(grid) - 1:
            break
        trees += 1 if grid[row][col] == '#' else 0
    return trees


def main():
    lines = loadData().split('\n')

    print("\nPart 1")
    t31 = count_trees(lines, 3, 1)
    print(t31)

    print("\nPart 2")
    t11 = count_trees(lines, 1, 1)
    t51 = count_trees(lines, 5, 1)
    t71 = count_trees(lines, 7, 1)
    t12 = count_trees(lines, 1, 2)
    print(t31 * t11 * t51 * t71 * t12)


if __name__ == "__main__":
    main()
