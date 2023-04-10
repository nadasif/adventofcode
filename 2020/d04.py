import re

from lib.mylib import loadData


def in_range(value: str, min_val: int, max_val: int) -> bool:
    return value.isdigit() and (min_val <= int(value) <= max_val)


def valid_hgt(value: str) -> bool:
    ln = len(value)
    if ln < 4:
        return False
    num = value[:ln - 2]
    unit = value[ln - 2:]
    return (unit == 'cm' or unit == 'in') and \
        (in_range(num, 150, 193) if unit == 'cm' else in_range(num, 59, 76))


class Passport:
    __KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    __CLR = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def __init__(self, txt):
        self.__info = dict(map(lambda p: p.split(':'), txt.split()))

    def is_valid(self) -> bool:
        return all(map(lambda k: k in self.__info, Passport.__KEYS))

    def is_valid2(self) -> bool:
        info = self.__info
        return self.is_valid() and \
            in_range(info['byr'], 1920, 2002) and \
            in_range(info['iyr'], 2010, 2020) and \
            in_range(info['eyr'], 2020, 2030) and \
            re.match(r'^#[0-9a-f]{6}$', info['hcl']) and \
            info['ecl'] in Passport.__CLR and \
            valid_hgt(info['hgt']) and \
            info['pid'].isdigit() and len(info['pid']) == 9


def main():
    passports = list(map(Passport, loadData().split('\n\n')))

    txt = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

    passports2 = list(map(Passport, txt.split('\n\n')))

    print("\nPart 1")
    print(len(list(filter(Passport.is_valid, passports))))

    print("\nPart 2")
    print(len(list(filter(Passport.is_valid2, passports))))


if __name__ == "__main__":
    main()
