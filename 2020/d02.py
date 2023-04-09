import re

from lib.mylib import loadData


class Policy:
    def __init__(self, txt):
        *nums, self.__chr = re.split(r'-([0-9]+) ', txt)
        self.__min, self.__max = map(int, nums)

    def __repr__(self):
        return f'<Policy {self.__min}-{self.__max} {self.__chr}>'

    def test(self, password: str) -> bool:
        return self.__min <= password.count(self.__chr) <= self.__max

    def test2(self, password):
        return (password[self.__min - 1] == self.__chr) != (password[self.__max - 1] == self.__chr)


class Password:
    def __init__(self, txt):
        policy_txt, self.__password = txt.split(': ')
        self.__policy = Policy(policy_txt)

    def __repr__(self):
        return f'<Password {self.__password}; {self.__policy}>'

    def is_valid(self):
        return self.__policy.test(self.__password)

    def is_valid2(self):
        return self.__policy.test2(self.__password)


def main():
    passwords = list(map(Password, loadData().split('\n')))

    print("\nPart 1")
    print(len(list(filter(lambda pwd: pwd.is_valid(), passwords))))

    print("\nPart 2")
    print(len(list(filter(lambda pwd: pwd.is_valid2(), passwords))))


if __name__ == "__main__":
    main()
