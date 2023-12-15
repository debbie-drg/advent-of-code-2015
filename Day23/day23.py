import sys


def perform_instructions(
    instructions: list[list[str]], start_a_value: int = 0
) -> dict[str, int]:
    registers = {"a": start_a_value, "b": 0}
    pointer = 0
    while pointer < len(instructions):
        current_instruction = instructions[pointer]
        pointer_changed = False
        match current_instruction[0]:
            case "hlf":
                registers[current_instruction[1]] //= 2
            case "tpl":
                registers[current_instruction[1]] *= 3
            case "inc":
                registers[current_instruction[1]] += 1
            case "jmp":
                pointer += int(current_instruction[1])
                pointer_changed = True
            case "jie":
                if registers[current_instruction[1].removesuffix(",")] % 2 == 0:
                    pointer += int(current_instruction[2])
                    pointer_changed = True
            case "jio":
                if registers[current_instruction[1].removesuffix(",")] == 1:
                    pointer += int(current_instruction[2])
                    pointer_changed = True
        if not pointer_changed:
            pointer += 1
    return registers


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    instructions = [
        instruction.split(" ")
        for instruction in open(file_name).read().strip().split("\n")
    ]
    registers = perform_instructions(instructions)
    print(
        f"The value of registry b after performing the instructions is {registers['b']}"
    )
    registers = perform_instructions(instructions, 1)
    print(
        f"If a starts as 1, it's {registers['b']}"
    )