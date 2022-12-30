import sys


def final_floor(lift_moves: str) -> int:
    return sum([instruction == "(" for instruction in lift_moves]) - sum(
        [instruction == ")" for instruction in lift_moves]
    )


def first_time_basement(lift_moves: str) -> int:
    instruction_values = {"(": 1, ")": -1}
    current_position = 0
    for index, instruction in enumerate(lift_moves):
        current_position += instruction_values[instruction]
        if current_position == -1:
            return index + 1


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    lift_moves = open(file_name).read()

    print(f"The final floor is {final_floor(lift_moves)}.")
    print(
        f"The number of moves until basement reached is {first_time_basement(lift_moves)}."
    )
