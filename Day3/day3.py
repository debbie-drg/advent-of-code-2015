import sys

DIRECTIONS_DICT = {"^": (1, 0), "v": (-1, 0), ">": (0, 1), "<": (0, -1)}

def sum_tuple(tuple_1: tuple[int, int], tuple_2: tuple[int, int]) -> tuple[int, int]:
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])

def houses_visited(instructions: str) -> int:
    visited = {(0,0)}
    location = (0,0)
    for instruction in instructions:
        location = sum_tuple(location, DIRECTIONS_DICT[instruction])
        visited.add(location)
    return len(visited)

def houses_visited_with_robot(instructions: str) -> int:
    visited = {(0,0)}
    santa_location = (0,0)
    robosanta_location = (0,0)
    for index, instruction in enumerate(instructions):
        if index % 2 == 0:
            santa_location = sum_tuple(santa_location, DIRECTIONS_DICT[instruction])
            visited.add(santa_location)
        else:
            robosanta_location = sum_tuple(robosanta_location, DIRECTIONS_DICT[instruction])
            visited.add(robosanta_location)
    return len(visited)

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    instructions = open(file_name).read()
    print(f"Santa visits a total of {houses_visited(instructions)} houses.")

    print(f"With the robot, they can visit {houses_visited_with_robot(instructions)} houses.")
