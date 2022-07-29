import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

lines = '''2138862165
2726378448
3235172758
6281242643
4256223158
1112268142
1162836182
1543525861
1882656326
8844263151'''

lines2 = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''


class Octopus:
    def __init__(self, row, col, e):
        self._flashed = False
        key = Key.get(row, col)
        Octopus.all[key] = self
        self._energy = int(e)
        self._neighbours = set()
        logger.debug('Creating Octopus [%s, %s]: %s', row, col, e)
        for r in range(row - 1 if row > 0 else 0, row + 2):
            for c in range(col - 1 if col > 0 else 0, col + 2):
                k = Key.get(r, c)
                logger.debug('  Key: %s', k)
                if key is not k and k in Octopus.all:
                    Octopus.all[k].addNeighbor(self)
        logger.debug('  Neighbors: %s', self._neighbours)

    def addNeighbor(self, o):
        if o not in self._neighbours:
            self._neighbours.add(o)
            o.addNeighbor(self)

    def increase(self):
        self._energy += 1 if self._energy < 10 else 0

    def flash(self):
        if not self._flashed and self._energy > 9:
            self._flashed = True
            for o in self._neighbours:
                o.increase()
                o.flash()

    @staticmethod
    def steps():
        # Step 1: increase levels
        for k, v in Octopus.all.items():
            v.increase()

        # Step 2: Flash
        for k, v in Octopus.all.items():
            v.flash()

        # Step 3: Cool down
        count = 0
        for k, v in Octopus.all.items():
            v._flashed = False
            if v._energy > 9:
                count += 1
                v._energy = 0
        return count

    def __repr__(self):
        d, m = divmod(self._energy, 10)
        return f'{m}'


Octopus.all = {}


class Key:
    def __init__(self, r, c):
        self._row = r
        self._col = c

    @staticmethod
    def get(r, c):
        key = f'{r},{c}'
        if key not in Key.keys:
            Key.keys[key] = Key(r, c)
        return Key.keys[key]

    def __repr__(self):
        return f'{self._row},{self._col}'


Key.keys = {}


def main():
    r = 0
    for line in lines.split('\n'):
        c = 0
        for o in line.strip():
            Octopus(r, c, o)
            c += 1
        r += 1

    total = 0
    allFlashed = 0
    for i in range(100):
        show()
        flashCount = Octopus.steps()
        if flashCount == 100:
            allFlashed = i + 1
        total += flashCount
    show()

    i = 100
    while flashCount != 100:
        flashCount = Octopus.steps()
        i += 1

    print(total)
    print(f'Step {i} all flashed')


def show():
    r = '0'
    for k, v in Octopus.all.items():
        nr = str(k).split(',')[0]
        if r != nr:
            r = nr
            print()
        print(v, end='')
    print('\n----------')


if __name__ == '__main__':
    main()
