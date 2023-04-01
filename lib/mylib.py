import inspect
import re


def loadData() -> str:
    infile = re.sub(r"(d[0-9]{2})\.py", r"in-\g<1>.txt", inspect.stack()[1].filename)
    with open(infile, "r") as file:
        return file.read().strip()
