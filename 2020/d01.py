from lib.mylib import loadData


def find_2sum(lst: list[int], target: int) -> int:
    seen = dict()
    for n in lst:
        if n in seen:
            return seen[n] * n
        seen[target - n] = n
    return 0


def find_3sum(unsorted_lst: list[int], target: int) -> int:
    lst = sorted(unsorted_lst)
    for i, n in enumerate(lst):
        two_sum = find_2sum(lst[i + 1:], target - n)
        if two_sum:
            return two_sum * n
    return 0


def main():
    nums = list(map(int, loadData().split('\n')))
    # print(nums)
    print("\nPart 1")
    print(find_2sum(nums, 2020))

    print("\nPart 2")
    print(find_3sum(nums, 2020))


if __name__ == "__main__":
    main()
