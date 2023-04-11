from functools import reduce

from lib.mylib import loadData


def main():
    groups = loadData().split('\n\n')
    print(groups)
    print("\nPart 1")
    print(sum(map(lambda s: len(set(s.replace('\n', ''))), groups)))

    print("\nPart 2")
    print()

    print(len(groups))
    total = 0
    for members in groups:
        all_yes = set(members)
        for member in members.split('\n'):
            all_yes &= set(member)
        #print(len(all_yes))
        total += len(all_yes)
    print(total)



if __name__ == "__main__":
    main()
