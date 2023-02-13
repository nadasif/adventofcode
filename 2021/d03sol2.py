import logging.config

logging.config.fileConfig('../logging.conf')
logger = logging.getLogger(__name__)


def main():
    file1 = open('d03in.txt', 'r')
    lines = file1.readlines()
    file1.close()

    # Convert all to int to avoid converting each time.
    # c0:[5, 7, 4, 5, 7], c1:[7, 5, 8, 7, 5]
    maxsize, nums = convertToInt(lines)
    sigBit = 1 << (maxsize - 1)

    count0, count1 = countZeroOneAtPos(nums, sigBit)
    lstOGR, lstCSR = distribute(nums, count0, count1, sigBit)
    sigBit >>= 1
    ogr = findOGR(lstOGR, sigBit)
    csr = findCSR(lstCSR, sigBit)

    print(f'{ogr * csr}')


def convertToInt(lines):
    maxsize = 0
    nums = []
    for line in lines:
        line = line.strip()
        nums.append(int(line, 2))
        maxsize = max(maxsize, len(line))
        logger.debug(f'{line}')
    return maxsize, nums


def countZeroOneAtPos(nums, sigBit):
    c0 = 0
    c1 = 0
    for num in nums:
        if num & sigBit:
            c1 += 1
        else:
            c0 += 1
    logger.debug(f'{sigBit:0b}, {c0}, {c1}')
    return c0, c1


def distribute(nums, c0, c1, sigBit):
    ogr = []
    csr = []
    for num in nums:
        if isOGR(num, c0, c1, sigBit):
            ogr.append(num)
        if isCSR(num, c0, c1, sigBit):
            csr.append(num)

    logger.debug(f'{ogr} {csr}')
    return ogr, csr


def isOGR(num, c0, c1, sigBit):
    return (c1 >= c0 and (num & sigBit)) or (c0 > c1 and (~num & sigBit))


def isCSR(num, c0, c1, sigBit):
    return (c0 <= c1 and (~num & sigBit)) or (c1 < c0 and (num & sigBit))


def findOGR(nums, sigBit):
    logger.debug('Finding OGR in %s at position %s', nums, sigBit)
    if len(nums) < 3:
        result = nums[0]
        if len(nums) > 1 and isOGR(nums[1], 1, 1, sigBit):
            result = nums[1]
        logger.debug('Found OGR as %s', result)
        return result

    c0, c1 = countZeroOneAtPos(nums, sigBit)
    ogr, csr = distribute(nums, c0, c1, sigBit)
    return findOGR(ogr, sigBit >> 1)


def findCSR(nums, sigBit):
    logger.debug('Finding CSR in %s at position %s', nums, sigBit)
    if len(nums) < 3:
        result = nums[0]
        if len(nums) > 1 and isCSR(nums[1], 1, 1, sigBit):
            result = nums[1]
        logger.debug('Found CSR as %s', result)
        return result

    c0, c1 = countZeroOneAtPos(nums, sigBit)
    ogr, csr = distribute(nums, c0, c1, sigBit)
    return findCSR(csr, sigBit >> 1)


if __name__ == '__main__':
    main()
