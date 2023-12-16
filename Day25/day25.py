import sys, re


def get_value(position: int):
    start = 20151125
    for _ in range(position):
        start = (start * 252533) % 33554393
    return start


def grid_to_position(row: int, col: int):
    diagonal = row + col
    below_rows = diagonal * (diagonal + 1) // 2
    return below_rows + col


def grid_to_value(row: int, col: int):
    return get_value(grid_to_position(row - 1, col - 1))


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    input_text = open(file_name).read().strip()
    row, col = [int(number) for number in re.findall("[0-9]+", input_text)]
    print(f"The number at row {row} and column {col} is {grid_to_value(row, col)}.")
