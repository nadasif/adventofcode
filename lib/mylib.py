import inspect
import re


class Stream:
    def __init__(self, iterable):
        self.__iterable = iterable

    def map(self, function):
        return Stream(map(function, self.__iterable))

    def list(self):
        return list(self.__iterable)

    def sum(self):
        return sum(self.__iterable)


def loadData() -> str:
    infile = re.sub(r"(d[0-9]{2})\.py", r"in-\g<1>.txt", inspect.stack()[1].filename)
    with open(infile, "r") as file:
        return file.read().strip()
