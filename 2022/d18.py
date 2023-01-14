import os
from collections import defaultdict, deque


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def main():
    txt = loadData('.in')

    lines = txt.split('\n')

    faces = defaultdict(int)
    offsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0), ]
    mnx, mny, mnz = [float('inf')] * 3
    mxx, mxy, mxz = [-float('inf')] * 3

    droplet = set()

    for line in lines:
        x, y, z = cell = tuple(map(int, line.split(',')))
        droplet.add(cell)
        mnx, mny, mnz = min(mnx, x), min(mny, y), min(mnz, z)
        mxx, mxy, mxz = max(mxx, x), max(mxy, y), max(mxz, z)
        for dx, dy, dz in offsets:
            k = (x + dx, y + dy, z + dz)
            faces[k] += 1

    mnx -= 1
    mny -= 1
    mnz -= 1
    mxx += 1
    mxy += 1
    mxz += 1

    print("\nPart 1")
    print(list(faces.values()).count(1))

    print("\nPart 2")

    air = {(mnx, mny, mnz)}
    q = deque([(mnx, mny, mnz)])

    print(q)
    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in offsets:
            nx, ny, nz = k = (x + dx * 2, y + dy * 2, z + dz * 2)
            if not (mnx <= nx <= mxx and mny <= ny <= mxy and mnz <= nz <= mxz):
                continue

            if k in droplet or k in air:
                continue

            air.add(k)
            q.append(k)

    free = set()
    for x, y, z in air:
        for dx, dy, dz in offsets:
            free.add((x + dx, y + dy, z + dz))

    print(len(set(faces) & free))


if __name__ == "__main__":
    main()
