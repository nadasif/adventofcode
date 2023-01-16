import os.path


def loadData():
    filename = f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt"
    f = open(filename, "r")
    txt = f.read().strip()
    f.close()
    return txt

def main():
    txt = loadData()

    print("Part 1")

    print("Part 1")


if __name__ == "__main__":
    main()
