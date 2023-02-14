import os


class Wire:
    def __init__(self, name):
        self.name = name
        self.value = -1

    def setValue(self):
        pass


class Gate:
    def __init__(self, txt):
        pass


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()


def main():
    txt = loadData()
    txt = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''
    print([l.split(' -> ') for l in txt.split("\n")])

    print("\nPart 1")

    print("\nPart 2")


if __name__ == "__main__":
    main()
