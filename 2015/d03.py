import os
from collections import defaultdict

class Santa:

    def __init__(self):
        self.pos = 0

    def next(self, homes, d):
        self.pos += d
        homes[self.pos] += 0


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def main():
    txt = loadData()

    MOVES = {'>': 1, '<': -1, '^': 1j, 'v': -1j}
    dirs = [MOVES[c] for c in txt]

    print("\nPart 1")
    homes = defaultdict(int)
    s = Santa()
    s.next(homes, 0)
    for d in dirs:
        s.next(homes, d)
    print(len(homes))

    print("\nPart 2")
    homes.clear()
    s = [Santa(), Santa()]
    for i, d in enumerate(dirs):
        s[i%2].next(homes,d)
    print(len(homes))


if __name__ == "__main__":
    main()
