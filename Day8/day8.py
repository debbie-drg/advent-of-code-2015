import sys

EMPTY_STRING_SIZE = sys.getsizeof("")


def in_memory_size(string_line: str):
    return len(string_line) - len(eval(string_line))


def encoded_size_difference(string_line: str):
    return 2 + string_line.count("\\") + string_line.count('"')


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    strings = open(file_name).read().strip().split("\n")

    result = sum(map(in_memory_size, strings))
    print(f"The literal minus in memory number of characters is {result}.")

    result_2 = sum(map(encoded_size_difference, strings))
    print(f"The encoded size minus the initial size is {result_2}.")
