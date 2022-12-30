import sys


class LightGarden:
    def __init__(self, number_rows, number_cols, brightness_mode=False):
        if not brightness_mode:
            self.lights = [[False] * number_rows for _ in range(number_cols)]
        else:
            self.lights = [[False] * number_rows for _ in range(number_cols)]
        self.brighness_mode = brightness_mode

    @staticmethod
    def parse_instruction(instruction: str, brightness_mode=False):
        split_instruction = instruction.split(" ")
        if split_instruction[0] == "toggle":
            intervals_at = [1, 3]
            action = 2 if brightness_mode else "toggle"
        else:
            intervals_at = [2, 4]
            if brightness_mode:
                action = 1 if split_instruction[1] == "on" else -1
            else:
                action = True if split_instruction[1] == "on" else False
        start_range = [
            int(element) for element in split_instruction[intervals_at[0]].split(",")
        ]
        end_range = [
            int(element) for element in split_instruction[intervals_at[1]].split(",")
        ]
        return action, start_range, end_range

    def perform_instruction(self, instruction: str):
        action, start_range, end_range = self.parse_instruction(instruction)
        if action == "toggle":
            for row_index in range(start_range[0], end_range[0] + 1):
                for col_index in range(start_range[1], end_range[1] + 1):
                    self.lights[row_index][col_index] = not self.lights[row_index][
                        col_index
                    ]
        else:
            for row_index in range(start_range[0], end_range[0] + 1):
                for col_index in range(start_range[1], end_range[1] + 1):
                    self.lights[row_index][col_index] = action

    def perform_instruction_brightness(self, instruction: str):
        action, start_range, end_range = self.parse_instruction(instruction, True)
        for row_index in range(start_range[0], end_range[0] + 1):
            for col_index in range(start_range[1], end_range[1] + 1):
                self.lights[row_index][col_index] += action
                self.lights[row_index][col_index] = max(
                    0, self.lights[row_index][col_index]
                )

    def value_lights_on(self):
        return sum([sum(row) for row in self.lights])

    def perform_instruction_batch(self, instruction_batch: list[str]):
        if self.brighness_mode:
            for instruction in instruction_batch:
                self.perform_instruction_brightness(instruction)
        else:
            for instruction in instruction_batch:
                self.perform_instruction(instruction)


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    instructions = open(file_name).read().strip().split("\n")
    garden = LightGarden(1000, 1000)
    garden.perform_instruction_batch(instructions)

    print(f"The total number of lights on is {garden.value_lights_on()}.")

    brightness_garden = LightGarden(1000, 1000, True)
    brightness_garden.perform_instruction_batch(instructions)

    print(f"The total brightness value is {brightness_garden.value_lights_on()}.")
