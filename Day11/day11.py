import sys

VALID_LETTERS = list("abcdefghjkmnpqrstuvwxyz")
ALL_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
REPEATED_LETTERS = [f"{letter}{letter}" for letter in VALID_LETTERS]
THREE_SEQUENCE = [
    f"{ALL_LETTERS[index]}{ALL_LETTERS[index + 1]}{ALL_LETTERS[index + 2]}"
    for index in range(len(ALL_LETTERS) - 2)
]
FORBIDDEN_LETTERS = ["i", "l", "o"]


def is_password_valid(password: list[str]) -> bool:
    return sum([sequence in password for sequence in REPEATED_LETTERS]) >= 2 and any(
        [sequence in password for sequence in THREE_SEQUENCE]
    )


def next_password(password: str) -> str:
    index = len(password) - 1
    password = list(password)
    while True:
        character = password[index]
        character_index = VALID_LETTERS.index(character)
        if character_index == len(VALID_LETTERS) - 1:
            password[index] = VALID_LETTERS[0]
            index -= 1
            if index < 0:
                return "".join(password)
        else:
            password[index] = VALID_LETTERS[character_index + 1]
            return "".join(password)


def list_of_strings_to_string(strings: list[str]) -> str:
    return_string = ""
    for string in strings:
        return_string += string
    return string


def next_non_forbidden(password: str) -> str:
    forbidden_position = dict()
    for element in FORBIDDEN_LETTERS:
        try:
            forbidden_position[element] = password.index(element)
        except ValueError:
            pass
    letter_to_change = min(forbidden_position, key=forbidden_position.get)
    index = forbidden_position[letter_to_change]
    password = list(password)
    password[index] = chr(ord(letter_to_change) + 1)
    password[index + 1 :] = ["a" for _ in range(index + 1, len(password))]
    return "".join(password)


def next_valid_password(password: str) -> str:
    if any(element in password for element in FORBIDDEN_LETTERS):
        password = next_non_forbidden(password)
    while True:
        password = next_password(password)
        if is_password_valid(password):
            return password


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    santa_password = open(file_name).read().strip()
    santa_password = next_valid_password(santa_password)
    print(f"The next valid password is {santa_password}.")
    santa_password = next_valid_password(santa_password)
    print(f"The next one after that is {santa_password}.")
