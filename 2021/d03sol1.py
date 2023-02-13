import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
    file1 = open('d03in.txt', 'r')
    lines = file1.readlines()
    file1.close()

    c0 = []  # Count zeros
    c1 = []  # Count ones

    for line in lines:
        data = line.strip()
        size = len(data)
        num = int(data, 2)

        for i in range(size):
            # Adjust the size of lists
            if i + 1 > len(c0):
                c0.append(0)
                c1.append(0)

            bit = num & (1 << (size - i - 1))
            if bit:
                c1[i] += 1
            else:
                c0[i] += 1

        logger.debug(f'{data}:{num:0{size}b} ==> {c0}, {c1} ')

    # Now calculate the gamma and epsilon
    size = len(c0)
    gamma = 0
    epsilon = 0
    for i in range(size):
        gamma <<= 1
        epsilon <<= 1
        if c1[i] > c0[i]:  # It means ONE is most common and ZERO is least common
            gamma += 1
        else:
            epsilon += 1
        logger.debug(f'Testing {c1[i]}, {c0[i]} ==> {gamma:0{size}b}:{gamma}, {epsilon:0{size}b}: {epsilon}')

    print(f'{gamma * epsilon}')


if __name__ == '__main__':
    main()
