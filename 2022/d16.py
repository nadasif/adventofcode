import os
from collections import deque

class Valve:

    def __init__(self, txt):
        self.name = txt.split()[1]
        self.flow = int(txt.split(";")[0].split("=")[1])
        self.targets = txt.split("to ")[1].split(" ", 1)[1].split(", ")
        self.dists = {}
        self.bit = 0

    def setBit(self, bit):
        self.bit = bit

    def addDistance(self, name, distance):
        self.dists[name] = distance

    def __repr__(self):
        return f"#<Valve: {self.name} -> {self.dists} ({self.flow}) [{self.bit:b}] >"

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
    valves = {}
    for line in lines:
        valve = Valve(line)
        valves[valve.name] = valve

    for valve in valves.values():
        if valve.name != 'AA' and not valve.flow:
            continue
        visited = {valve.name}
        queue = deque([(0, valve)])
        while queue:
            d, v = queue.popleft()
            for n in v.targets:
                if n in visited:
                    continue
                visited.add(n)
                neighbor = valves[n]
                if neighbor.flow:
                    valve.addDistance(n, d+1)
                queue.append((d+1, neighbor))

    for index, valve in enumerate(sorted(filter(lambda v: valves[v].flow>0, valves))):
        valves[valve].setBit(1 << index)
        print(valves[valve])

    goodCount = index + 1

    cache = {}
    def dfs(time, curValve: Valve, bitmask):
        if (time, curValve, bitmask) in cache:
            return cache[(time, curValve, bitmask)]

        maxFlow = 0
        for name in curValve.dists:
            bit = valves[name].bit
            if bitmask & bit:
                continue
            remTime = time - (curValve.dists[name] + 1)
            if remTime <= 0:
                continue
            maxFlow = max(maxFlow, valves[name].flow * remTime + dfs(remTime, valves[name], bitmask | bit))

        cache[(time, curValve, bitmask)] = maxFlow
        return maxFlow

    print("\nPart 1")
    print(dfs(30, valves['AA'], 0))

    print("\nPart 2")
    b = (1 << goodCount) - 1
    print(f"{b} : {b:b} ")
    max2 = 0
    for i in range((b+1) // 2):
        max2 = max(max2, dfs(26, valves['AA'], i) + dfs(26, valves['AA'], b ^ i))
    print(max2)


if __name__ == "__main__":
    main()
