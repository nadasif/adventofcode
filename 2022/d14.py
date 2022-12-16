import os

class Part1:
    def __init__(self, txt):
        pass

    def __repr__(self):
        return f"#<P1:>"

class Part2:
    def __init__(self, txt):
        pass

    def __repr__(self):
        return f"#<P2:>"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    txt = loadData('.in')
    lines = txt.split('\n')

    print("\nPart 1")

    print("\nPart 2")


    pass


if __name__ == "__main__":
    main()
