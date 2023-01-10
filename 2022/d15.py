import os

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def parseXY(txt):
    return tuple(map(int, txt.split("x=")[1].split(", y=")))

def parse(txt):
    sb = txt.split(":")
    return parseXY(sb[0]), parseXY(sb[1])

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def main():
    txt = loadData('.in')
    lines = txt.split('\n')
    sensors = []
    beacons = set()
    dists = []
    r = []
    y = 2000000
    for i in range(len(lines)):
        s, b = parse(lines[i])
        d = dist(s,b)
        sensors.append(s)
        beacons.add(b)
        dists.append(d)

        if abs(s[1] - y) <= d:
            r.append(i)

    min_x = max_x = sensors[r[0]][0]
    for i in r:
        s = sensors[i]
        d = dists[i]
        dx = d - abs(s[1] - y)
        min_x = min(min_x, s[0] - dx)
        max_x = max(max_x, s[0] + dx)

    c = 0
    for x in range(min_x, max_x+1):
        if (x,y) not in beacons:
            b = False
            for i in r:
                if dist((x,y), sensors[i]) <= dists[i]:
                    b = True
                    break
            c += 1 if b else 0


    print("\nPart 1")
    print(f"{c}")

    print("\nPart 2")
    pLines = []
    nLines = []
    for i in range(len(sensors)):
        s = sensors[i]
        d = dists[i]
        pLines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
        nLines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

    pos = neg = None
    N = len(pLines)
    for i in range(N):
        for j in range(i+1, N):
            a, b = pLines[i], pLines[j]
            if abs(a-b) == 2:
                pos = min(a,b) + 1

            a, b = nLines[i], nLines[j]
            if abs(a-b) == 2:
                neg = min(a,b) + 1

    x, y = (pos + neg) // 2, (pos - neg) // 2
    print(f'{x}, {y} -> {x * 4000000 + y}')
    pass


if __name__ == "__main__":
    main()
