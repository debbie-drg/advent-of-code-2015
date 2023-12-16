import sys
from copy import copy
from functools import reduce

mul = lambda x, y: x * y


def quantum_entaglement(packages, number_groups: int = 3) -> int:
    groups, min_len = get_groups(
        packages=packages, number_groups=number_groups, groups=[]
    )
    groups = [group for group in groups if len(group) == min_len]
    entanglement = min([reduce(mul, group) for group in groups])
    del groups
    return entanglement


def get_groups(
    packages: list[int],
    all_packages: list[int] = [],
    total_value: int = -1,
    value_to_match: int = -1,
    current_group: list[int] = [],
    groups: list[list[int]] = [],
    min_len: int = 100,
    number_groups: int = 3,
) -> tuple[list[list[int]], int]:
    if value_to_match == -1:
        all_packages = copy(packages)
        value_to_match = sum(packages) // number_groups
        total_value = value_to_match
    if len(current_group) >= min_len:
        return groups, min_len
    for index, package in enumerate(packages):
        if package > value_to_match:
            continue
        now_group = copy(current_group)
        now_group.append(package)
        remaining_packages = [
            package for package in all_packages if package not in now_group
        ]
        if package == value_to_match and is_group_valid(
            remaining_packages, total_value, total_value, number_groups - 1
        ):
            group_len = len(current_group) + 1
            if group_len <= min_len:
                min_len = min(group_len, min_len)
                groups.append(copy(now_group))
            min_len = min(min_len, len(current_group) + 1)
        else:
            groups, min_len = get_groups(
                packages[index + 1 :],
                all_packages,
                total_value,
                value_to_match - package,
                now_group,
                groups,
                min_len,
                number_groups,
            )
    return groups, min_len


def is_group_valid(
    remaining_packages: list[int],
    value_to_match: int,
    total_value: int,
    number_groups: int,
):
    if value_to_match in remaining_packages:
        if number_groups == 2:
            return True
        index = remaining_packages.index(value_to_match)
        if is_group_valid(
            remaining_packages[:index] + remaining_packages[index + 1 :],
            total_value,
            total_value,
            number_groups - 1,
        ):
            return True
    for index, package in enumerate(remaining_packages):
        if value_to_match < package:
            continue
        if is_group_valid(
            remaining_packages[index + 1 :],
            value_to_match - package,
            total_value,
            number_groups,
        ):
            return True
    return False


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    packages = [int(package) for package in open(file_name).read().strip().splitlines()]
    packages.reverse()
    print(
        f"The quantun entaglement for the best arrangement is {quantum_entaglement(packages)}"
    )
    print(f"With four groups, it's {quantum_entaglement(packages, 4)}")
