import sys


def sum_all_integers(input_data, ignore_red=False):
    integer_sum = 0
    if isinstance(input_data, int):
        integer_sum += input_data
    elif isinstance(input_data, str):
        pass
    elif isinstance(input_data, list):
        for element in input_data:
            integer_sum += sum_all_integers(element, ignore_red)
    elif isinstance(input_data, dict):
        if ignore_red and ("red" in input_data.values()):
            return integer_sum
        for element in input_data.values():
            integer_sum += sum_all_integers(element, ignore_red)
    return integer_sum


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    input_string = open(file_name).read().strip()
    input_data = eval(input_string)
    sum_of_integers = sum_all_integers(input_data)
    print(f"The sum of all integers in the input is {sum_of_integers}.")

    sum_ignoring_red = sum_all_integers(input_data, True)
    print(f"If red is ignored, the sum is {sum_ignoring_red}.")
