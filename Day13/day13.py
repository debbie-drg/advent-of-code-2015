import sys
from itertools import permutations


class Table:
    def __init__(self, happiness_scores: list[str]) -> None:
        self.people = self.get_number_people(happiness_scores)
        self.happines_scores = [[0] * len(self.people) for _ in range(len(self.people))]
        for line in happiness_scores:
            person_1_index = self.people.index(line[0])
            person_2_index = self.people.index(line[-1].removesuffix("."))
            happiness_score = int(line[3]) if line[2] == "gain" else -int(line[3])
            self.happines_scores[person_1_index][person_2_index] = happiness_score

    @staticmethod
    def get_number_people(happiness_scores: list[str]) -> list[str]:
        people = set()
        for line in happiness_scores:
            people.add(line[0])
            people.add(line[-1].removesuffix("."))
        return list(people)

    def get_best_happiness_score(self) -> int:
        max_score = -1e10
        number_people = len(self.people)
        for permutation in permutations(range(len(self.people))):
            current_score = 0
            for index in range(len(permutation)):
                person = permutation[index]
                left = permutation[(index - 1) % number_people]
                right = permutation[(index + 1) % number_people]
                current_score += self.happines_scores[person][left]
                current_score += self.happines_scores[person][right]
            max_score = max(max_score, current_score)
        return max_score

    def add_yourself(self):
        self.people.append("yourself")
        for line in self.happines_scores:
            line.append(0)
        self.happines_scores.append([0] * len(self.people))


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    happiness_scores = [
        line.split(" ") for line in open(file_name).read().strip().split("\n")
    ]
    table_arrangement = Table(happiness_scores)
    print(
        f"The maximum possible happiness score is {table_arrangement.get_best_happiness_score()}."
    )
    table_arrangement.add_yourself()
    print(
        f"After adding yourself, the maximum possible happiness score is {table_arrangement.get_best_happiness_score()}."
    )
