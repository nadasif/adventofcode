import os

class Rock:
    def __init__(self, func):
        self.func = func

    def rock(self, dx, dy):
        return {(x+dx, y) for (x,y) in self.func(dy)}

    def __repr__(self):
        return f"#<Rock: {self.func(1)}>"

def summarize(solid):
    o = [0] * 7
    for x,y in solid:
        o[x] = max(o[x], y)
    top = max(o)
    return tuple(x - top for x in o)


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    txt = loadData('.in')
    N = len(txt)
    jets = [1 if x == '>' else -1 for x in txt]

    rocks = [
        Rock(lambda y: {(0,y), (1,y), (2,y), (3,y)}),
        Rock(lambda y: {(1,y), (0, y+1), (1, y+1), (2, y+1), (1, y+2)}),
        Rock(lambda y: {(0,y), (1,y), (2,y), (2, y+1), (2, y+2)}),
        Rock(lambda y: {(0, y), (0, y+1), (0, y+2), (0, y+3)}),
        Rock(lambda y: {(0, y), (1, y), (0, y+1), (1, y+1)}),
    ]


    def findHeight(T):
        seen = {}

        height = 0
        rc = 0
        ri = 0
        rock = rocks[ri].rock(2, height + 3)
        solid = Rock(lambda y: {(x, y) for x in range(7)}).rock(0, -1)
        ji = 0
        while rc < T:
            jet = jets[ji]
            moved = {(x+jet, y) for (x,y) in rock} # Jet applied
            if all(0 <= x < 7 for (x,y) in moved) and not (moved & solid):
                rock = moved

            moved = {(x, y-1) for (x,y) in rock} # move down
            if moved & solid:
                solid |= rock
                rc += 1
                ri = (ri + 1) % 5
                height = max(y for (x,y) in solid) + 1
                rock = rocks[ri].rock(2, height + 3)

                key = (ji, ri, summarize(solid))
                if key in seen:
                    lrc, lh = seen[key]
                    rem = T - rc
                    rep = rem // (rc - lrc)
                    offset = rep * (height - lh)
                    rc += rep * (rc - lrc)
                    seen = {}
                seen[key] = (rc, height)

            else:
                rock = moved
            ji = (ji + 1) % N
        return height + offset

    print("\nPart 1")
    print(findHeight(2022))

    print("\nPart 2")
    print(findHeight(1000000000000))


    pass


if __name__ == "__main__":
    main()
