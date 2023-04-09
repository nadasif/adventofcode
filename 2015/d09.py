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
        dists = ", ".join([f"{k.name}:{v}" for k, v in self.distances.items()])
        return f'City({self.name!r} {dists})'

    def set_distance(self, city, dist):
        self.distances[city] = dist

    def __shortest_distance(self, visited):
        visited[self] = visited.get(self) or 0
        cities = set(self.distances.keys()) - set(visited.keys())
        if cities:
            city = min(cities, key=self.distances.get)
            visited[city] = self.distances[city]
            city.__shortest_distance(visited)
        return visited

    def shortest_route(self):
        visited = self.__shortest_distance(dict())
        print({c.name: d for c, d in visited.items()})
        return sum(visited.values())

    def __longest_distance(self, visited):
        visited[self] = visited.get(self) or 0
        cities = set(self.distances.keys()) - set(visited.keys())
        if cities:
            city = max(cities, key=self.distances.get)
            visited[city] = self.distances[city]
            city.__longest_distance(visited)
        return visited

    def longest_route(self):
        visited = self.__longest_distance(dict())
        print({c.name: d for c, d in visited.items()})
        return sum(visited.values())

    @classmethod
    def create_city(cls, txt):
        name1, name2, dist = re.split(r' to | = ', txt)
        city1 = City.cities.get(name1) or cls(name1)
        city2 = City.cities.get(name2) or cls(name2)
        city1.set_distance(city2, int(dist))
        city2.set_distance(city1, int(dist))


def main():
    txt = loadData()
    list(map(City.create_city, txt.split('\n')))
    for city in City.cities.values():
        print(city)
    print("\nPart 1")
    print(min(map(lambda c: c.shortest_route(), list(City.cities.values()))))

    print("\nPart 2")
    print(max(map(lambda c: c.longest_route(), City.cities.values())))


if __name__ == "__main__":
    main()
