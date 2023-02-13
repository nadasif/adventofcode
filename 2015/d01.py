import os


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def zero(floor, n):
    floor[0] += n
    return floor[0] == -1

def main():
    txt = loadData()
    lst = list(map(lambda c: 1 if c=='(' else -1, txt))
    # c -> c=="(" ? 1 : 0

    print("Part 1")
    print(sum(lst))

    print("Part 1")
    floor = [0]
    print(1 + next(filter( lambda i: zero(floor, lst[i]), range(len(lst)) )))


if __name__ == "__main__":
    main()
