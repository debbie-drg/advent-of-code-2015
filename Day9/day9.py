import sys
from itertools import permutations


class CityDistances:
    def __init__(self, distance_list: list[str]):
        self.cities = []
        for line in distance_list:
            if line[0] not in self.cities:
                self.cities.append(line[0])
            if line[2] not in self.cities:
                self.cities.append(line[2])
        self.number_cities = len(self.cities)
        self.distances = [[0] * self.number_cities for _ in range(self.number_cities)]
        for line in distance_list:
            index_city_1 = self.cities.index(line[0])
            index_city_2 = self.cities.index(line[2])
            self.distances[index_city_1][index_city_2] = int(line[4])
            self.distances[index_city_2][index_city_1] = int(line[4])

    def find_minimum_distance(self) -> int:
        min_distance = 1e64
        for permutation in permutations(range(self.number_cities)):
            min_distance = min(min_distance, self.permutation_distance(permutation))
        return min_distance

    def find_maximum_distance(self) -> int:
        max_distance = 0
        for permutation in permutations(range(self.number_cities)):
            max_distance = max(max_distance, self.permutation_distance(permutation))
        return max_distance

    def permutation_distance(self, permutation) -> int:
        distance = 0
        for index in range(len(permutation) - 1):
            distance += self.distances[permutation[index]][permutation[index + 1]]
        return distance


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    distance_list = open(file_name).read().strip().split("\n")
    distance_list = [line.split(" ") for line in distance_list]
    city_distances = CityDistances(distance_list)

    print(
        f"The minimum distance to traverse every city is {city_distances.find_minimum_distance()}."
    )
    print(f"The maximum distance is {city_distances.find_maximum_distance()}.")
