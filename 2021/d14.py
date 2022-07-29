import os
from collections import defaultdict


class Poly:
    def __init__(self):
        self.template = []
        self.pairs = dict()
        pass

    def read(self, s: str):
        if s == '':
            return
        pair = s.split(' -> ')
        if len(pair) > 1:
            self.pairs[pair[0]] = pair[1]
        else:
            self.template = s
        pass

    def step(self, itr):
        chain = self.template
        pairs = self.pairs
        count = defaultdict(int)
        pCount1 = defaultdict(int)
        count[chain[0]] = 1
        for j in range(1, len(chain)):
            pCount1[chain[j - 1] + chain[j]] += 1
            count[chain[j]] += 1

        for i in range(itr):
            keys = list(filter(lambda p: pCount1[p] > 0, pCount1.keys()))
            pCount2 = defaultdict(int)
            for k in keys:
                l = k[0]
                r = k[1]
                c = pairs[k]
                n = pCount1[k]
                pCount2[l + c] += n
                pCount2[c + r] += n
                count[c] += n
            pCount1 = pCount2
        sums = sorted(count.items(), key=lambda v: v[1])
        print(sums)
        hi = sums[len(sums) - 1][1]
        lo = sums[0][1]
        print(f'{hi} - {lo} = {hi - lo}')


def main():
    poly = Poly()
    loadData('.in', poly)
    print(poly.template)
    poly.step(10)
    print('--------------- Part 1')
    poly.step(40)
    print('--------------- Part 2')


def loadData(ext: str, poly: Poly):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        poly.read(line.strip())


if __name__ == "__main__":
    main()
