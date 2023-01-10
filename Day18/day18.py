import sys

NEIGHBOURS = {(1, 0), (1, 1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (1, -1)}


def sum_tuples(tuple_1: tuple[int, int], tuple_2: tuple[int, int]) -> tuple[int, int]:
    return (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])


class LightAnimation:
    def __init__(self, light_initial_status: list[str], corners_on: bool = False):
        self.height = len(light_initial_status)
        self.width = len(light_initial_status[0])
        self.lights = set()
        self.corners_on = corners_on
        for hor_index, line in enumerate(light_initial_status):
            for ver_index, character in enumerate(line):
                if character == "#":
                    self.lights.add((hor_index, ver_index))
        if self.corners_on:
            self.add_corners(self.lights)

    def add_corners(self, lights):
        lights.update(
            [
                (0, 0),
                (0, self.width - 1),
                (self.height - 1, 0),
                (self.height - 1, self.width - 1),
            ]
        )

    def get_neighbours(self, position: tuple[int, int]) -> set[tuple[int, int]]:
        neighbours = set()
        for neighbour in NEIGHBOURS:
            neighbours.add(sum_tuples(position, neighbour))
        return neighbours

    def get_on_neighbours(self, position: tuple[int, int]) -> int:
        return len(self.get_neighbours(position).intersection(self.lights))

    def next_step(self) -> bool:
        next_lights = set()
        for hor_index in range(self.height):
            for ver_index in range(self.width):
                number_neighbours = self.get_on_neighbours((hor_index, ver_index))
                if number_neighbours == 3 or (
                    number_neighbours == 2 and (hor_index, ver_index) in self.lights
                ):
                    next_lights.add((hor_index, ver_index))
        if self.corners_on:
            self.add_corners(next_lights)
        if self.lights == next_lights:
            return True
        self.lights = next_lights
        return False

    def multiple_steps(self, number_steps: int):
        for _ in range(number_steps):
            if self.next_step():
                break

    def number_lights_on(self):
        return len(self.lights)

    def __repr__(self) -> str:
        representation = ""
        for hor_index in range(self.height):
            for ver_index in range(self.width):
                if (hor_index, ver_index) in self.lights:
                    representation += "#"
                else:
                    representation += "."
            representation += "\n"
        return representation


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    light_initial_status = open(file_name).read().strip().split("\n")
    light_animation = LightAnimation(light_initial_status)
    light_animation.multiple_steps(100)
    print(f"After 100 steps, there are {light_animation.number_lights_on()} lights on.")

    light_animation = LightAnimation(light_initial_status, True)
    light_animation.multiple_steps(100)
    print(
        f"If the corner lights stay on, the number is {light_animation.number_lights_on()}."
    )
