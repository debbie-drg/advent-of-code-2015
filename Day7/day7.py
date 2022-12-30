import sys

NUMBER_BITS = 16


class Wires:
    def __init__(self):
        self.wire_values = dict()

    def try_retrieve_value(self, key: str):
        if key.isnumeric():
            return int(key)
        try:
            return self.wire_values[key]
        except KeyError:
            return None

    def perform_instruction(self, instruction: str) -> bool:
        split_instructions = instruction.split(" ")
        if len(split_instructions) == 3:
            value = self.try_retrieve_value(split_instructions[0])
            if value is None:
                return False
            self.wire_values[split_instructions[2]] = value
            return True
        if split_instructions[0] == "NOT":
            value = self.try_retrieve_value(split_instructions[1])
            if value is None:
                return False
            self.wire_values[split_instructions[3]] = (
                ~value + 2**NUMBER_BITS
            )
            return True
        value_1 = self.try_retrieve_value(split_instructions[0])
        value_2 = self.try_retrieve_value(split_instructions[2])
        if value_1 is None or value_2 is None:
            return False
        instruction = split_instructions[1]
        receiving_variable = split_instructions[4]
        if instruction == "AND":
            self.wire_values[receiving_variable] = value_1 & value_2
        elif instruction == "OR":
            self.wire_values[receiving_variable] = value_1 | value_2
        elif instruction == "LSHIFT":
            self.wire_values[receiving_variable] = value_1 << value_2
        elif instruction == "RSHIFT":
            self.wire_values[receiving_variable] = value_1 >> value_2
        else:
            raise AssertionError
        return True

    def perform_instructions_batch(self, instructions: list[str]):
        while instructions:
            to_remove = []
            for index, instruction in enumerate(instructions):
                if self.perform_instruction(instruction):
                    to_remove.append(index)
            instructions = [instructions[index] for index in range(len(instructions)) if index not in to_remove]
    
    def override_and_perform(self, instructions: list[str], value_to_take: str, value_to_replace: str):
        self.wire_values = {value_to_replace : self.wire_values[value_to_take]}
        to_remove = []
        for index, instruction in enumerate(instructions):
            if instruction.split(" ")[-1] == value_to_replace:
                to_remove.append(index)
        instructions = [instructions[index] for index in range(len(instructions)) if index not in to_remove]
        self.perform_instructions_batch(instructions)



if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    instructions = open(file_name).read().strip().split("\n")

    wires = Wires()
    wires.perform_instructions_batch(instructions)
    print(f"The value of wire a is {wires.wire_values['a']}.")

    wires.override_and_perform(instructions, "a", "b")
    print(f"After overriding wire b with the value of wire a, the value of wire a is {wires.wire_values['a']}.")
