import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


class Bingo:

    def __init__(self, lines):
        self.lastNum = -1
        self.nums = {}
        groups = []

        for line in lines:
            nums = []
            sNums = line.strip().split()
            for sNum in sNums:
                num = int(sNum)
                self.nums[num] = False
                nums.append(num)
            groups.append(nums)

        for i in range(5):
            col = []
            for j in range(5):
                col.append(groups[j][i])
            groups.append(col)

        self.groups = groups

    def mark(self, num):
        self.lastNum = num
        self.nums[num] = True

    def isBingo(self) -> bool:
        return self._isBingo(self.groups)

    def _isBingo(self, lst) -> bool:
        for nums in self.groups:
            result = True
            for num in nums:
                result = result and self.nums[num]
            if result:
                return True
        return False

    def score(self) -> int:
        s = 0
        for num in self.nums:
            s += 0 if self.nums[num] else num

        return s * self.lastNum

    def reset(self):
        for k in self.nums:
            self.nums[k] = False

    def __str__(self):
        result = f'{self.nums}'
        return result


def main():
    file1 = open('d04in.txt', 'r')
    lines = file1.readlines()
    file1.close()

    # Read the random numbers first
    nums = list(map(lambda x: int(x), lines[0].strip().split(',')))
    games: list[Bingo] = []

    for i in range(1, len(lines), 6):
        bingo = Bingo(lines[i + 1:i + 6])
        games.append(bingo)

    # Part One result
    winner = findWinner(games, nums)
    print(f'Score: {winner.score()}')

    # Part Two result
    winner = findLastWinner(games, nums) or winner
    print(f'Score: {winner.score()}')


def findWinner(games, nums) -> Bingo:
    for num in nums:
        for game in games:
            game.mark(num)
            if game.isBingo():
                return game
    return None


def findLastWinner(games, nums) -> Bingo:
    winner = None
    for num in nums:
        for game in list(filter(lambda x: not x.isBingo(), games)):
            game.mark(num)
            if game.isBingo():
                winner = game
    return winner


if __name__ == '__main__':
    main()
