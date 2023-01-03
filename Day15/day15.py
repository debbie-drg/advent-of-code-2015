from __future__ import annotations
import sys


def fixed_length_partitions(number: int, number_partitions: int):
    if number_partitions == 1:
        yield (number,)
    else:
        for i in range(0, number):
            for p in fixed_length_partitions(number - i, number_partitions - 1):
                yield (i,) + p
        yield (number,) + tuple([0] * (number_partitions - 1))


class Ingredient:
    def __init__(self, ingredient_properties: list[str]):
        properties = [ingredient_properties[index] for index in [2, 4, 6, 8, 10]]
        self.properties = [int(value.removesuffix(",")) for value in properties]


class IngredientCombination:
    def __init__(self, ingredient_data: list[list[str]]):
        self.ingredients = [Ingredient(line) for line in ingredient_data]

    def score(self, number_tablespoons: int, number_calories: int | None = None) -> int:
        max_score = int(-1e10)
        for partition in fixed_length_partitions(
            number_tablespoons, len(self.ingredients)
        ):
            if (
                number_calories is not None
                and self.calorie_count(partition) != number_calories
            ):
                continue
            current_score = self.partition_score(partition)
            max_score = max(max_score, current_score)
        return max_score

    def partition_score(self, partition: tuple[int]) -> int:
        score = 1
        for index in range(4):
            score *= max(
                0,
                sum(
                    [
                        partition[ingredient_index] * ingredient.properties[index]
                        for ingredient_index, ingredient in enumerate(self.ingredients)
                    ]
                ),
            )
        return score

    def calorie_count(self, partition: tuple[int]) -> int:
        calories = 0
        for index in range(len(self.ingredients)):
            calories += partition[index] * self.ingredients[index].properties[4]
        return calories


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"

    ingredient_data = [
        line.split(" ") for line in open(file_name).read().strip().split("\n")
    ]
    ingredient_combinations = IngredientCombination(ingredient_data)
    max_score = ingredient_combinations.score(100)
    print(f"The max attainable score is {max_score}.")
    max_score_500_calories = ingredient_combinations.score(100, number_calories=500)
    print(
        f"If we only take recipees with 500 calories, we get a score of {max_score_500_calories}."
    )
