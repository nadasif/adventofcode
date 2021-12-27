import os

paths = {'': 0}


class Node:
    def __init__(Self, data, r, c, p):
        Self.r = r
        Self.c = c
        Self.w = data['lines'][r][c]
        Self.p = p
        Self.f = 0
        Self.g = 0
        Self.h = data['rows'] - r + data['cols'] - c - 2

    def isLocSame(Self, node):
        return Self.r == node.r and Self.c == node.c

    def __repr__(Self):
        return f'N({Self.r},{Self.c},{Self.w},{Self.f},{Self.h})'


def byF(node: Node):
    return node.f


def main():
    data = loadData('.sd')
    print(f"Processing {data['cols']} x {data['rows']}")
    # print(f'{paths}')
    # path(data, '', 38)
    # print(f'{paths}')

    findPath(data)

def findPath(data):
    start = Node(data, 0, 0, None)
    end = Node(data, data['rows'] - 1, data['cols'] - 1, None)
    print(f'First Node: {start}')
    print(f'Last Node: {end}')
    lst = successors(data, start, end)
    print(f'Next: {lst}')
    

def successors(data, node, dest):
    lst = []
    if node.r > 0:
        lst.append(Node(data, node.r - 1, node.c, node))
    if node.r < dest.r:
        lst.append(Node(data, node.r + 1, node.c, node))
    if node.c > 0:
        lst.append(Node(data, node.r, node.c - 1, node))
    if node.c < dest.c:
        lst.append(Node(data, node.r, node.c + 1, node))
    return lst

def findPathOld(data):
    dest = Node(data, data['rows'] - 1, data['cols'] - 1, None)
    openList = [Node(data, 0, 0, None)]
    closedList = []

    while len(openList) > 0:
        openList.sort(key=byF)
        print(f'Open  : {openList}')
        print(f'Closed: {closedList}')
        q = openList.pop()
        print(f'{q}')

        # Find successors
        successors = []
        if q.r > 0:
            successors.append(Node(data, q.r - 1, q.c, q))
        if q.r < dest.r:
            successors.append(Node(data, q.r + 1, q.c, q))
        if q.c > 0:
            successors.append(Node(data, q.r, q.c - 1, q))
        if q.c < dest.c:
            successors.append(Node(data, q.r, q.c + 1, q))

        # Now reject or accept the successors
        for s in successors:
            skipNode = q.p and s.isLocSame(q.p)
            if s.isLocSame(dest):
                openList.clear()
                break

            s.g = q.g + 1
            s.f = s.g + s.h + s.w + q.w

            for n in openList:
                if n.isLocSame(s) and n.f < s.f:
                    skipNode = True
            for n in closedList:
                if n.isLocSame(s) and n.f < s.f:
                    skipNode = True

            if not skipNode:
                openList.append(s)
        print(f'Next: {successors}')

        closedList.append(q)


def distLeft(r, c, dr, dc):
    return abs(r - dr) + abs(c - dc)


def loadData(ext):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    lines = list(map(lambda l: [int(c) for c in l.strip()], file.readlines()))
    file.close()
    d = {'rows': len(lines), 'cols': len(lines[0]), 'lines': lines}

    return d


if __name__ == "__main__":
    main()
