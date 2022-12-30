import sys
from math import prod

def parse_gift_size(sizes: str) -> list[int]:
    return [int(size) for size in sizes.split("x")]


def side_area(box_size: list[int]) -> list[int]:
    side_1 = box_size[0] * box_size[1]
    side_2 = box_size[0] * box_size[2]
    side_3 = box_size[1] * box_size[2]
    return [side_1, side_2, side_3]


def wrapping_paper_size(box_size: list[int]) -> int:
    side_1, side_2, side_3 = side_area(box_size)
    min_side = min([side_1, side_2, side_3])
    return 2 * (side_1 + side_2 + side_3) + min_side


def ribbon_length(box_size: list[int]) -> int:
    sides = sorted(box_size)
    return 2 * (sides[0] + sides[1]) + prod(sides)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    gift_sizes = open(file_name).read()
    gift_sizes = gift_sizes.strip().split("\n")

    parsed_gifts = list(map(parse_gift_size, gift_sizes))

    wrapping_paper = sum(map(wrapping_paper_size, parsed_gifts))
    print(f"We need a total of {wrapping_paper} square feet of wrapping paper.")

    ribbon = sum(map(ribbon_length, parsed_gifts))
    print(f"We need a total of {ribbon} feet of ribbon.")
