import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.mylib import loadDataNew



def main():
    lines = loadDataNew().split("\n")

    #nums = list(map(int, loadDataNew().split('\n')))
    list1, list2 = zip(*[map(int, item.split()) for item in lines])
    list1, list2 = sorted(list(list1)), sorted(list(list2))
    print("\nPart 1")
    differences = sum([abs(a - b) for a, b in zip(list1, list2)])
    print(differences)

    print("\nPart 2")


if __name__ == "__main__":
    main()
