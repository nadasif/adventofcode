import os


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def main():
    txt = loadData()

    print("\nPart 1")

    print("\nPart 2")


if __name__ == "__main__":
    main()
