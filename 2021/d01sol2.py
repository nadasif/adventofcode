import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
    file1 = open('d01in.txt', 'r')
    lines = file1.readlines()
    file1.close()

    count = 0
    lastSum = -1
    queue = []

    for line in lines:
        num = int(line.strip())
        queue.append(num)
        if len(queue) < 3:
            pass
        elif len(queue) == 3:
            lastSum = sum(queue)
        else:
            queue.pop(0)
            currSum = sum(queue)

            if currSum > lastSum:
                status = '(inc)'
                count += 1
            else:
                status = '(same/less)'
            lastSum = currSum

        logger.debug('%s, %s', num, queue)

    print(f'{count}')


if __name__ == "__main__":
    main()
