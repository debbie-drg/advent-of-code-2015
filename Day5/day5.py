import sys

VOWELS = {"a", "e", "i", "o", "u"}
BAD_STRINGS = ["ab", "cd", "pq", "xy"]


def is_nice(input_string: str) -> bool:
    if sum([element in VOWELS for element in input_string]) < 3:
        return False
    if any([string in input_string for string in BAD_STRINGS]):
        return False
    for index in range(len(input_string) - 1):
        if input_string[index] == input_string[index + 1]:
            return True
    return False


def new_is_nice(input_string: str) -> bool:
    for index in range(len(input_string) - 1):
        current_pair = input_string[index : index + 2]
        if current_pair in input_string[index + 2 :]:
            break
    else:
        return False
    for index in range(len(input_string) - 2):
        if input_string[index] == input_string[index + 2]:
            return True
    return False


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    string_list = open(file_name).read().strip().split("\n")
    number_nice_strings = sum(map(is_nice, string_list))
    new_number_nice_strings = sum(map(new_is_nice, string_list))

    print(f"The number of nice strings is {number_nice_strings}.")
    print(
        f"With the new rules, the number of nice strings is {new_number_nice_strings}."
    )
