import os.path
import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)

lined = '''1721
979
366
299
675
1456'''.split()

def loadData():
    filename = f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt"
    file1 = open(filename, 'r')
    text = file1.read().strip()
    file1.close()
    return text

def main():
    lines = loadData().split('\n')

    nums = list(map(int, lines))

    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                logger.debug('%s, %s: %s', nums[i], nums[j], nums[i] * nums[j])

    pair = findPair(2020, lines)

    print(f'{pair[0] * pair[1]}')


def findPair(target, lines):
    comps = {}
    for line in lines:
        num = int(line.strip())
        comp = target - num
        if comp in comps:
            return [num, comp]
        comps[num] = 1
        logger.debug('%s for %s', num, comps)

    raise RuntimeError("Not found")


if __name__ == '__main__':
    main()
