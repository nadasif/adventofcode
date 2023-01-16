import os.path


def loadData():
    filename = f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt"
    f = open(filename, "r")
    txt = f.read().strip()
    f.close()
    return txt

def basement(lst):
    s = 0
    for i, n in enumerate(lst):
        s += n
        if s < 0:
            return i + 1
    return 0

def main():
    txt = loadData()
    lst = list(map(lambda c: 1 if c=='(' else -1, txt))

    print("Part 1")
    print(sum(lst))

    print("Part 1")
    print(basement(lst))


if __name__ == "__main__":
    main()
