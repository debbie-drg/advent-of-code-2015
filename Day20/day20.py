import sys


def find_first_house(min_presents: int) -> int:
    min_presents //= 10
    presents_per_house = [0] * min_presents
    for i in range(1, min_presents):
        for j in range(i, min_presents, i):
            presents_per_house[j] += i * 10
        if presents_per_house[i] >= 10*min_presents:
            return i
    raise AssertionError

def find_first_house_bis(min_presents: int) -> int:
    presents_per_house = [0] * (min_presents // 11)
    loop_length = len(presents_per_house)
    for i in range(1, loop_length):
        houses_visited = 0
        for j in range(i, loop_length, i):
            houses_visited += 1
            if houses_visited > 50:
                break
            presents_per_house[j] += i * 11
        if presents_per_house[i] >= min_presents:
            return i
    print(max(presents_per_house))
    raise AssertionError


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    input_value = int(open(file_name).read().strip())
    print(f"The first house to get at least {input_value} presents is {find_first_house(input_value)}.")
    print(f"If instead each elf only visits 50 houses but leaves 11 presents, the first one is {find_first_house_bis(input_value)}.")

