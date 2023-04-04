import re

from lib.mylib import loadData


class City:
    cities = dict()

    def __init__(self, name):
        self.name = name
        self.distances = dict()
        City.cities[name] = self

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return hash(other) == hash(self)

    def __repr__(self):
        dists = ", ".join([f"{k}:{v}" for k, v in self.distances.items()])
        return f'City({self.name!r} {dists})'

    def set_distance(self, node, dist):
        if self.distances.get(node.name) is None:
            self.distances[node.name] = dist
            node.set_distance(self, dist)

    @classmethod
    def create_city(cls, txt):
        name1, name2, dist = re.split(r' to | = ', txt)
        city1 = City.cities.get(name1) or cls(name1)
        city2 = City.cities.get(name2) or cls(name2)
        city1.set_distance(city2, int(dist))


def main():
    txt = loadData()
    list(map(City.create_city, txt.split('\n')))
    for city in City.cities.values():
        print(city)
    print("\nPart 1")

    print("\nPart 2")


if __name__ == "__main__":
    main()
