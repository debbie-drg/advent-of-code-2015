import sys


def look_and_say_iteration(input_string: str) -> str:
    output_string = ""
    current_character = input_string[0]
    count = 0
    for character in input_string:
        if character == current_character:
            count += 1
        else:
            output_string += f"{count}{current_character}"
            current_character = character
            count = 1
    if count != 0:
        output_string += f"{count}{current_character}"
    return output_string


def look_and_say_multiple(input_string: str, number_times: int) -> str:
    for _ in range(number_times):
        input_string = look_and_say_iteration(input_string)
    return input_string


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    input_string = open(file_name).read().strip()
    input_string = look_and_say_multiple(input_string, 40)
    print(f"After 40 iterations, the string has a length of {len(input_string)}.")
    input_string = look_and_say_multiple(input_string, 10)
    print(f"After 50 iterations, the length is already {len(input_string)}.")
