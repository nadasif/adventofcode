from . import InvoiceLine

def parseLine(txt: str):
    s = txt.split(" at ")
    price = float(s[1])
    s = s[0].split(' ', 2)
    qty = int(s[0])
    name = s[1]
    return InvoiceLine(name, qty, price)