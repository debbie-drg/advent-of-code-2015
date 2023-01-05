import sys


def find_combinations_adding(containers: list[int], capacity: int):
    containers_used = [0] * (len(containers) + 1)
    containers_used = _find_combinations_adding(
        containers, capacity, containers_used, 0
    )
    return containers_used


def _find_combinations_adding(
    containers: list[int],
    capacity: int,
    containers_used: list[int],
    number_containers: int,
) -> list[int]:
    if capacity == 0:
        containers_used[number_containers] += 1
        return containers_used
    if capacity < 0 or not containers:
        return containers_used
    containers_used = _find_combinations_adding(
        containers[1:],
        capacity - containers[0],
        containers_used,
        number_containers + 1,
    )
    containers_used = _find_combinations_adding(
        containers[1:], capacity, containers_used, number_containers
    )
    return containers_used


def find_combinations_using_minimum(combinations: list[int]) -> tuple[int, int]:
    for index, value in enumerate(combinations):
        if value != 0:
            min_containers = index
            break
    else:
        raise ValueError("No valid combination exists.")
    return min_containers, value


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    containers = [int(line) for line in open(file_name).read().strip().split("\n")]

    capacity_to_match = 25 if "example" in file_name else 150
    number_combinations = find_combinations_adding(containers, capacity_to_match)
    print(
        f"There are {sum(number_combinations)} ways to store {capacity_to_match} liters."
    )
    min_containers, number_min_combinations = find_combinations_using_minimum(
        number_combinations
    )
    print(f"The minimum number of containers we can use is {min_containers}.")
    print(
        f"There are {number_min_combinations} ways of getting the desired capacity with this number of containers."
    )
