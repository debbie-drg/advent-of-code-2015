import sys

SUE_DATA = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

GREATER = {"cats", "trees"}
FEWER = {"pomeranians", "goldfish"}


def check_sue(sue_line: list[str], updated_info=False) -> bool:
    for index in [2, 4, 6]:
        try:
            current_key = sue_line[index].removesuffix(":")
            current_value = int(sue_line[index + 1].removesuffix(","))
            correct_sue_value = SUE_DATA[current_key]
            if updated_info and current_key in GREATER:
                if correct_sue_value >= current_value:
                    return False
            elif updated_info and current_key in FEWER:
                if correct_sue_value <= current_value:
                    return False
            elif correct_sue_value != current_value:
                return False
        except KeyError:
            continue
    return True


def find_correct_sue(sue_data: list[list[str]], updated_info=False) -> int:
    for sue in sue_data:
        if check_sue(sue, updated_info):
            return int(sue[1].removesuffix(":"))
    raise ValueError("Aunt Sue not found.")


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"

    sue_data = [line.split(" ") for line in open(file_name).read().strip().split("\n")]
    gifted_sue = find_correct_sue(sue_data)
    print(f"The Sue that gave you the gift was number {gifted_sue}.")

    updated_gifted_sue = find_correct_sue(sue_data, True)
    print(f"With the updated info, it was number {updated_gifted_sue}.")
