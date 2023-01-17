import os
import hashlib


def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def find_idx(txt, zCount):
    digest = '1' * zCount
    zeros = '0' * zCount
    idx = 0
    while digest[:zCount] != zeros:
        idx += 1
        digest = hashlib.md5(f'{txt}{idx}'.encode('ascii')).hexdigest()
    return idx


def main():
    txt = loadData()

    print("\nPart 1")
    print(find_idx(txt, 5))

    print("\nPart 1")
    print(find_idx(txt, 6))


if __name__ == "__main__":
    main()
