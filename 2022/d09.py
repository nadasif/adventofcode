import os

hx, hy, tx, ty = 0,0,0,0

def touching(x1, y1, x2, y2):
    return abs(x2-x1) <= 1 and abs(y2-y1) <= 1

def move(dx, dy):
    global hx, hy, tx, ty
    hx += dx
    hy += dy
    if not touching(hx, hy, tx, ty):
        tx += 0 if hx==tx else (hx-tx)/abs(hx-tx)
        ty += 0 if hy==ty else (hy-ty)/abs(hy-ty)

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    dxy = {'L': (-1,0), 'R':(1,0), 'U': (0,1), 'D': (0,-1)}

    txt = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
    txt = loadData('.in')
    visited = set()
    visited.add((tx,ty))

    lines = txt.split('\n')
    for line in lines:
        op, steps = line.split(' ')
        steps = int(steps)
        dx, dy = dxy[op]

        for _ in range(steps):
            move(dx, dy)
            visited.add((tx,ty))

    print(len(visited))
    pass


if __name__ == "__main__":
    main()
