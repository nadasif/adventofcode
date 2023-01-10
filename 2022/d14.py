import os

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def minmax(lst, x, y):
    print(f"{lst}; {x}, {y} --> ", end='')
    lst[0] = min([lst[0], x])
    lst[1] = max([lst[1], x])
    lst[2] = max([lst[2], y])
    print(f"{lst};")

def dot(x, y, rocks, drops):
    p = (x, y)
    if p in {(500, 0)}:
        return '+'
    elif p in rocks:
        return '#'
    elif p in drops:
        return 'o'
    else:
        return '.'

def drop2(filled, mxy):
    x, y = 500, 0
    if (x, y) in filled:
        return False

    while y <= mxy:
        if (x, y + 1) not in filled:
            y += 1
            continue

        if (x-1, y + 1) not in filled:
            x -= 1
            y += 1
            continue

        if (x+1, y + 1) not in filled:
            x += 1
            y += 1
            continue

        break

    filled.add((x,y))
    return True



def drop(filled, mxy):
    x, y = 500, 0
    while y <= mxy:
        ny = y + 1
        if (x, ny) not in filled:
            y += 1
            continue

        if (x-1, ny) not in filled:
            x -= 1
            y += 1
            continue

        if (x+1, ny) not in filled:
            x += 1
            y += 1
            continue

        filled.add((x,y))
        return True
    return False

def main():
    rocks = set()
    txt = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''
    txt = loadData('.in')
    lines = txt.split('\n')
    mmc = [500, 500,0]
    for line in lines:
        coords = line.split(" -> ")
        x1, y1 = eval(coords[0])
        for i in range(1, len(coords)):
            x2, y2 = eval(coords[i])
            minmax(mmc, x2, y2)
            if y1 != y2:
                assert x1 == x2
                ds = sorted([y1, y2])
                for d in range(ds[0], ds[1] + 1):
                    rocks.add((x1, d))
            if x1 != x2:
                assert y1 == y2
                ds = sorted([x1, x2])
                for d in range(ds[0], ds[1] + 1):
                    rocks.add((d, y1))

            x1, y1 = x2, y2

    drops = set(rocks)
    print("\nPart 1")
    i = 0
    while drop(drops, mmc[2]):
        i += 1
    print(i)



    drops = set(rocks)
    while drop2(drops, mmc[2]):
        pass

    print("\nPart 2")
    print(len(drops) - len(rocks))

if __name__ == "__main__":
    main()
